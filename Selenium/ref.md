# Selenium Tutorial 

## Installation 
Ref - https://www.selenium.dev/documentation/en/selenium_installation/

## Chromium Drive download 
Ref - https://sites.google.com/a/chromium.org/chromedriver/

## Sample Code: 

### Find Element & Elements 
```
-Example-01

let {Builder, By} = require('selenium-webdriver');
driver = new Builder().forBrowser('firefox').build();

(async function test(){

//Navigate to url
await driver.get('http://www.google.com');

// Get search box element from webElement 'q' using Find Element
let searchBar = driver.findElement(By.name('q'));

//Perform action using WebElement
await searchBar.sendKeys('Webdriver');

})();
  
- Example-02

const {Builder, By} = require('selenium-webdriver');
(async function example() {
    let driver = await new Builder().forBrowser('firefox').build();
    try {
        // Navigate to Url
        await driver.get('https://www.example.com');

        // Get all the elements available with tag 'p'
        let elements = await driver.findElements(By.css('p'));
        for(let e of elements) {
            console.log(await e.getText());
        }
    }
    finally {
        await driver.quit();
    }
})();
  
```
### Find Element From Element
```
let {Builder, By} = require('selenium-webdriver');
driver = new Builder().forBrowser('firefox').build();

(async function test(){

//Navigate to url
await driver.get('http://www.google.com');

//Get and store DOM element '<form>'
let searchForm = driver.findElement(By.name('f'));

//Get search box element from webElement 'form'
let searchBar = searchForm.findElement(By.name('q'));

//Perform action using WebElement
await searchBar.sendKeys('Webdriver');

})();
  
```

### Get Active Element
```
const {Builder, By} = require('selenium-webdriver');

(async function example() {
    let driver = await new Builder().forBrowser('chrome').build();
    await driver.get('https://www.google.com');
    await  driver.findElement(By.css('[name="q"]')).sendKeys("webElement");

    // Get attribute of current active element
    let attr = await driver.switchTo().activeElement().getAttribute("title");
    console.log(`${attr}`)
})();

```
