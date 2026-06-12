# OPTIER SDK Architecture

## Design Philosophy

The OPTIER SDK is designed as a high-level Python interface over the OEM HTTP API.

SDK users should never need to know:

- Raw HTTP endpoints
- Raw JSON structures
- Cookie handling
- CSRF handling
- Session management
- OEM error codes

The SDK is responsible for:

- Authentication
- Session lifecycle
- Heartbeat
- Error mapping
- Request/Response parsing
- Python object abstraction

--------------------------------------------------

OEM HTTP API

            │

            ▼

     Internal Request Engine

            │

            ▼

      Internal Error Mapping

            │

            ▼

      Python Exception Layer

            │

            ▼

       High Level SDK Objects

            │

            ▼

         SDK User Code
