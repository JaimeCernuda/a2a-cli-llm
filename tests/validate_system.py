#!/usr/bin/env python3
"""Validation script for A2A CLI system."""

import asyncio
import httpx
import logging
from pathlib import Path
import sys
import uvicorn
import threading
import time

from server.main import create_server_app
from shared.core.config import ServerConfig, ClientConfig
from client.main import A2ACLIClient


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestServer:
    """Test server manager."""
    
    def __init__(self, host="localhost", port=8888):
        self.host = host
        self.port = port
        self.server = None
        self.thread = None
    
    def start(self):
        """Start the server in a background thread."""
        config = ServerConfig(host=self.host, port=self.port, log_level="warning")
        server_app = create_server_app(config)
        app = server_app.build()
        
        uvicorn_config = uvicorn.Config(
            app=app,
            host=self.host,
            port=self.port,
            log_level="warning"
        )
        
        self.server = uvicorn.Server(uvicorn_config)
        
        def run_server():
            asyncio.run(self.server.serve())
        
        self.thread = threading.Thread(target=run_server)
        self.thread.daemon = True
        self.thread.start()
        
        # Wait for server to start
        time.sleep(2)
        logger.info(f"Test server started on {self.host}:{self.port}")
    
    def stop(self):
        """Stop the server."""
        if self.server:
            self.server.should_exit = True
        if self.thread:
            self.thread.join(timeout=5)


async def test_client_server_communication():
    """Test complete client-server communication."""
    server = TestServer()
    
    try:
        # Start server
        logger.info("Starting test server...")
        server.start()
        
        # Test client communication
        logger.info("Testing client communication...")
        config = ClientConfig.from_url(f"http://localhost:{server.port}")
        
        async with A2ACLIClient(config) as client:
            # Test 1: Agent info
            logger.info("Test 1: Getting agent info...")
            await client.get_agent_info()
            logger.info("✓ Agent info retrieved successfully")
            
            # Test 2: Send simple message
            logger.info("Test 2: Sending simple message...")
            await client.send_message("Hello, agent!", streaming=False)
            logger.info("✓ Simple message sent successfully")
            
            # Test 3: Send greeting message
            logger.info("Test 3: Sending greeting...")
            await client.send_message("Hi there!", streaming=False)
            logger.info("✓ Greeting sent successfully")
            
            # Test 4: Request help
            logger.info("Test 4: Requesting help...")
            await client.send_message("help", streaming=False)
            logger.info("✓ Help request sent successfully")
            
            # Test 5: Echo test
            logger.info("Test 5: Testing echo...")
            await client.send_message("echo test message", streaming=False)
            logger.info("✓ Echo test sent successfully")
            
            # Test 6: Time request
            logger.info("Test 6: Requesting time...")
            await client.send_message("what time is it", streaming=False)
            logger.info("✓ Time request sent successfully")
            
            # Test 7: File upload (if sample file exists)
            sample_file = Path("examples/sample.txt")
            if sample_file.exists():
                logger.info("Test 7: Testing file upload...")
                await client.send_message("Analyze this file", str(sample_file), streaming=False)
                logger.info("✓ File upload test sent successfully")
            else:
                logger.info("Test 7: Skipped (sample file not found)")
            
        logger.info("All tests completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"Test failed: {e}")
        return False
    finally:
        logger.info("Stopping test server...")
        server.stop()


async def main():
    """Main validation function."""
    logger.info("=== A2A CLI System Validation ===")
    
    try:
        success = await test_client_server_communication()
        
        if success:
            logger.info("🎉 All validation tests passed!")
            logger.info("The A2A CLI system is working correctly.")
            return 0
        else:
            logger.error("❌ Validation tests failed!")
            return 1
            
    except Exception as e:
        logger.error(f"Validation failed with error: {e}")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)