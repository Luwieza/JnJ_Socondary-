"""
Compatibility shim: re-export production settings so `Recociliator_J.settings`
is importable locally and in deployments.
"""
from .settings_prod import *  # noqa: F401,F403

# Override any production settings here for local development
SECURE_SSL_REDIRECT = False
