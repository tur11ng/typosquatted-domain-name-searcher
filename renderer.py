import pyppeteer


class Renderer:
    _page = None

    @staticmethod
    async def render_text(text: str) -> bytes:
        if not Renderer._page:
            browser = await pyppeteer.launch()
            Renderer._page = await browser.newPage()

        content = f"""
        data:text/html,
        <html>
        <head>
            <style>
                body {{
                    font-family: arial; sans-serif;
                    font-size: 16px;
                }}
            </style>
        </head>
        <body>
            <a>{text}</a>
        </body>
        </html>
        """
        element = await Renderer._page.JJ('a')
        return await element[0].screenshot()
