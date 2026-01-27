# Backend Architecture

## Startup Flow
1. Load environment config
2. Initialize logger
3. Load Express app
4. Connect to database
5. Mount routes
6. Start HTTP server

## Folder Responsibilities
- config: Environment & configuration
- loaders: Application bootstrapping
- routes: HTTP route definitions
- controllers: Request handling
- services: Business logic
- repositories: Database access
- models: Database schemas
- middlewares: Express middlewares
- utils: Helpers (logger, constants)
- jobs: Background tasks
- logs: Application logs

## Architecture Pattern
Route → Controller → Service → Repository → Database
