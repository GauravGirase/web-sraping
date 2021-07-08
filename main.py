import asyncio
from pyppeteer import launch

from utility import contants
from utility.utility import populate_data_in_csv_file, loading
from utility.contants import LOADING_MSG


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(contants.url, {'waitUntil': 'domcontentloaded'})

    # user is being authenticate by using his credentials

    await page.evaluate(f"""() => {{
         document.getElementById('sign-in')[2].value = '{contants.email}';
         document.getElementById('sign-in')[3].value = '{contants.password}';
         document.getElementById('sign-in')[5].dispatchEvent(new MouseEvent('click', {{
               bubbles: true,
               cancelable: true,
               view: window
           }}));
     }}""")

    loading(LOADING_MSG[0][0], LOADING_MSG[1][1])
    await page.screenshot()
    await page.waitForSelector('footer')
    await page.screenshot()

    total_users = await page.evaluate('''() => {
                     return {
                         users : document.getElementById("table-group-users").rows.length
                     }
                 }''')

    # User's data that to be populated in csv file

    data = []

    for i in range(2, total_users['users']):
        await page.waitForSelector('footer')
        loading(LOADING_MSG[2][2], LOADING_MSG[3][3])
        await page.screenshot()

        await page.evaluate(f"""() => {{
                 document.getElementById("table-group-users").rows[{i}].querySelector('a').dispatchEvent(new MouseEvent('click', {{
                     bubbles: true,
                     cancelable: true,
                     view: window
                 }}));
             }}""")

        loading(LOADING_MSG[2][2], LOADING_MSG[3][3])
        await page.screenshot()

        # Individual user details extracted

        user_details = await page.evaluate('''() => {
                  return {
                      name: document.getElementsByClassName('box-body box-profile')[0].querySelector('h3').innerText,
                      email: document.getElementsByClassName('box-body box-profile')[0].querySelector('span').innerText,
                      lacale: document.getElementsByClassName('box-body box-profile')[0].querySelectorAll('p')[1].innerText,
                      roles: document.getElementsByClassName('box-body box-profile')[0].querySelectorAll('p')[2].innerText
                  }
              }''')

        data.append(user_details)
        await page.goBack()

    # Data that we extracted from above one, is going to populate in csv file for local usage

    populate_data_in_csv_file(data)

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
