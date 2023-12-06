import argparse
import logging.config
import pathlib
from contextlib import asynccontextmanager

import dotenv
import uvicorn
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from eidos import agent_os
from eidos.system.agent_machine import AgentMachine

dotenv.load_dotenv()

# Set up the argument parser
parser = argparse.ArgumentParser(description="Start a FastAPI server.")
parser.add_argument("-p", "--port", type=int, default=8080, help="Port to run the FastAPI server on. Defaults to 8080.")
parser.add_argument("-r", "--reload", help="Reload the server when the code changes. Defaults to False.", action="store_true")
parser.add_argument('--debug', action='store_true', help='Turn on debug logging')
parser.add_argument("yaml_path", type=str, help="Path to a directory containing YAML files describing the agent machine to start.")

# Parse command line arguments
args = parser.parse_args()


@asynccontextmanager
async def start_os(app: FastAPI):
    conf_ = pathlib.Path(__file__).parent.parent.parent / "logging.conf"
    logging.config.fileConfig(conf_)
    logger = logging.getLogger("eidolon")
    logger.setLevel(logging.DEBUG if args.debug else logging.INFO)
    try:
        machine = AgentMachine.from_dir(args.yaml_path)
        await machine.start(app)
        agent_os._machine = machine
    except Exception as e:
        logger.exception("Failed to start AgentOS")
        raise e
    yield
    await machine.stop()


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger = logging.getLogger("eidolon")
        logger.info(f"Request: {request.method} {request.url}")
        try:
            response = await call_next(request)
        except Exception as e:
            logger.exception("Unhandled exception")
            raise e
        logger.info(f"Response: {response.status_code}")
        return response


app = FastAPI(lifespan=start_os)
app.add_middleware(LoggingMiddleware)


if __name__ == "__main__":
    log_level_str = "debug" if args.debug else "info"

    # Run the server
    uvicorn.run("eidos.system.agent_http_server:app", host="0.0.0.0", port=args.port, log_level=log_level_str, reload=args.reload)
