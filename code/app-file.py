# Copyright (c) 2025 Microsoft Corporation.
# Licensed under the MIT License

"""
This file is the entry point for the NLWeb Sample App.

WARNING: This code is under development and may undergo changes in future releases.
Backwards compatibility is not guaranteed at this time.
"""

import asyncio
import os
import webbrowser
from webserver.WebServer import fulfill_request, start_server
from dotenv import load_dotenv


async def open_browser_after_delay(url, delay=2.0):
    """Open browser after a delay to ensure server is ready."""
    await asyncio.sleep(delay)
    print(f"Opening browser to {url}")
    webbrowser.open(url)


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get port from Azure environment or use default
    port = int(os.environ.get('PORT', 8000))
    
    # Create the URL to open
    url = f"http://localhost:{port}/static/str_chat.html"    # Start the browser opening task in the background first
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # Schedule the browser opening task
    loop.create_task(open_browser_after_delay(url))
    
    # Start the server (this will block)
    loop.run_until_complete(start_server(
        host='0.0.0.0',
        port=port,
        fulfill_request=fulfill_request
    ))

if __name__ == "__main__":
    main()