package OpenSUTD;

import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class Test_OpenSUTD_Home {
    @Test
    public void Find_all_links(){
        System.setProperty("webdriver.chrome.driver","C:\\webdrivers\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();

        options.addArguments("disable-infobars");
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        String domian = "http://192.168.99.100/";
        String openSutd = domian;
        driver.get(openSutd);

        // get all the links
        java.util.List<WebElement> links = driver.findElements(By.tagName("a"));
        System.out.println(links.size());

        System.out.println("***Prining all link names***");
        // print all the links
        for (int i = 0; i < links.size(); i=i+1) {
            System.out.println(i + " " + links.get(i).getText());
        }
        System.out.println("***Prining all link addresses***");
        // print all the hyper links
        for (int i = 0; i < links.size(); i=i+1) {
            System.out.println(i + " " + links.get(i).getAttribute("href"));
        }
    }

    @Test
    public void FindAndClickAllLink() throws InterruptedException{
        System.setProperty("webdriver.chrome.driver","C:\\webdrivers\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();

        options.addArguments("disable-infobars");
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        String domian = "http://192.168.99.100/";
        String openSutd = domian;
        driver.get(openSutd);


        // get all the links
        java.util.List<WebElement> links = driver.findElements(By.tagName("a"));
        System.out.println(links.size());

        // print all the links
        for (int i = 0; i < links.size(); i=i+1) {
            System.out.println(i + " " + links.get(i).getText());
            System.out.println(i + " " + links.get(i).getAttribute("href"));
        }

        // click all links in a web page
        for(int i = 0; i < links.size(); i++)
        {
            System.out.println("*** Navigating to" + " " + links.get(i).getAttribute("href"));
            if (links.get(i).getAttribute("href") != null && !links.get(i).getAttribute("href").equals(openSutd)) {
                boolean staleElementLoaded = true;
                while (staleElementLoaded) {
                    try {
                        driver.navigate().to(links.get(i).getAttribute("href"));
                        Thread.sleep(1000);
                        driver.navigate().back();
                        links = driver.findElements(By.tagName("a"));
                        System.out.println("*** Navigated to" + " " + links.get(i).getAttribute("href"));
                        staleElementLoaded = false;
                    } catch (StaleElementReferenceException e) {
                        staleElementLoaded = true;
                    }
                }
            }
        }
    }

    @Test
    public void Signin(){
        String myUserName = "superadmin";
        String myPassword = "asdf1234";

        System.setProperty("webdriver.chrome.driver","C:\\webdrivers\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();

        options.addArguments("disable-infobars");
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        String domian = "http://192.168.99.100/";
        String openSutd = domian;
        driver.get(openSutd);


        driver.findElement(By.linkText("SIGN IN")).click();

        // get the user name field of the account page
        driver.findElement(By.name("login")).sendKeys(myUserName);
        driver.findElement(By.name("password")).sendKeys(myPassword);

        driver.findElement(By.className("primaryAction")).click();

        Assert.assertTrue(driver.getCurrentUrl().equals(openSutd));
    }
}
