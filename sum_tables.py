import asyncio
from playwright.async_api import async_playwright

seed_urls = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=78",
    "https://sanand0.github.io/tdsdata/js_table/?seed=79",
    "https://sanand0.github.io/tdsdata/js_table/?seed=80",
    "https://sanand0.github.io/tdsdata/js_table/?seed=81",
    "https://sanand0.github.io/tdsdata/js_table/?seed=82",
    "https://sanand0.github.io/tdsdata/js_table/?seed=83",
    "https://sanand0.github.io/tdsdata/js_table/?seed=84",
    "https://sanand0.github.io/tdsdata/js_table/?seed=85",
    "https://sanand0.github.io/tdsdata/js_table/?seed=86",
    "https://sanand0.github.io/tdsdata/js_table/?seed=87",
]

async def main():
    total = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for url in seed_urls:
            await page.goto(url)
            await page.wait_for_selector("table")

            cells = await page.locator("td").all_text_contents()
            numbers = [int(x) for x in cells if x.isdigit()]
            total += sum(numbers)

        await browser.close()
    print(total)

asyncio.run(main())