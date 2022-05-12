import logging

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status


from api.endpoints.dependencies.db import get_db
from api.endpoints.dependencies.tenant_security import get_from_context

from api.services.v1 import governance_service

from api.db.repositories.tenant_schemas import TenantSchemasRepository
from api.db.models.tenant_schema import TenantSchemaRead
from api.endpoints.models.v1.governance import (
    SchemasListResponse,
    CreateSchemaPayload,
    ImportSchemaPayload,
)

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/", status_code=status.HTTP_200_OK, response_model=SchemasListResponse)
async def list_tenant_schemas(
    db: AsyncSession = Depends(get_db),
) -> SchemasListResponse:
    # TODO: add search/paging parameters
    # copy of v0 implementation from endpoints/routes/tenant_admin
    # this should take some query params, sorting and paging params...
    wallet_id = get_from_context("TENANT_WALLET_ID")
    schema_repo = TenantSchemasRepository(db_session=db)
    tenant_schemas = await schema_repo.find_by_wallet_id(wallet_id)

    response = SchemasListResponse(
        items=tenant_schemas, count=len(tenant_schemas), total=len(tenant_schemas)
    )
    return response


@router.post("/", status_code=status.HTTP_200_OK)
# Method moved from v0
async def create_tenant_schema(
    payload: CreateSchemaPayload,
    db: AsyncSession = Depends(get_db),
) -> TenantSchemaRead:
    # TODO: update to v1 response
    """
    Create a new schema and/or credential definition.

    "schema_request", defines the new schema.
    If "cred_def_tag" is provided, create a credential definition (which can be for a
    new or existing schema).
    """
    wallet_id = get_from_context("TENANT_WALLET_ID")
    tenant_id = get_from_context("TENANT_ID")
    return await governance_service.create_tenant_schema(
        db,
        wallet_id,
        tenant_id,
        payload.schema_request,
        None,
        payload.cred_def_tag,
        payload.revocable,
        payload.revoc_reg_size,
    )


@router.post("/import", status_code=status.HTTP_200_OK)
# Method moved from v0
async def import_tenant_schema(
    payload: ImportSchemaPayload,
    db: AsyncSession = Depends(get_db),
) -> TenantSchemaRead:
    # TODO: update to v1 response
    """
    Import an existing public schema and optionally create a credential definition.

    If "schema_id" is provided, use an existing schema.
    If "cred_def_tag" is provided, create a credential definition (which can be for a
    new or existing schema).
    """
    wallet_id = get_from_context("TENANT_WALLET_ID")
    tenant_id = get_from_context("TENANT_ID")
    return await governance_service.create_tenant_schema(
        db,
        wallet_id,
        tenant_id,
        None,
        payload.schema_id,
        payload.cred_def_tag,
        payload.revocable,
        payload.revoc_reg_size,
    )