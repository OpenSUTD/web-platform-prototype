package OpenSUTD;

import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class Test_OpenSUTD_Projects {

    @Test
    public void Find_all_links(){
        System.setProperty("webdriver.chrome.driver","C:\\webdrivers\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();

        options.addArguments("disable-infobars");
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        String domian = "http://192.168.99.100/";
        String openSutd = domian +"projects/";
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
        String openSutd = domian +"projects/";
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
                        Thread.sleep(3000);
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
    public void SearchProject() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver","C:\\webdrivers\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();

        options.addArguments("disable-infobars");
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        String domain = "http://192.168.99.100/";
        String openSutd = domain +"projects/";
        driver.get(openSutd);

        driver.findElement(By.name("title")).sendKeys("MOMOBOT");
        driver.findElement(By.name("title")).clear();
        driver.findElement(By.name("title")).sendKeys("DEEPLEARNING-WORKSHOP-2019");
        driver.findElement(By.xpath("/html/body/main/div/form/button")).click();

        Assert.assertTrue(driver.findElement(By.tagName("h4")).getText().equals("DEEPLEARNING-WORKSHOP-2019"));

        driver.navigate().to(driver.findElement(By.xpath("/html/body/main/div/div/div[1]/div/div/div/a")).getAttribute("href"));

        Assert.assertTrue(driver.getCurrentUrl().equals(domain + "projects/SELF_00011/"));
    }

    @Test
    public void SearchProjects() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver","C:\\webdrivers\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();

        options.addArguments("disable-infobars");
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        String domain = "http://192.168.99.100/";
        String openSutd = domain +"projects/";
        driver.get(openSutd);

        java.util.List<WebElement> titlesList = driver.findElements(By.tagName("h4"));

        String[] titles = new String[titlesList.size()];
        String[] links = new String[titlesList.size()];

        for (int i = 0; i < titlesList.size(); i=i+1) {
            links[i] = driver.findElement(By.xpath("/html/body/main/div/div/div[" + (i+1) + "]/div/div/div/a")).getAttribute("href");
            titles[i] = titlesList.get(i).getText();
        }

        for (int i = 0; i < titlesList.size(); i=i+1) {
            String title = titles[i];
            String link = links[i];
            driver.findElement(By.name("title")).sendKeys(title);
            driver.findElement(By.xpath("/html/body/main/div/form/button")).click();
            Assert.assertTrue(driver.findElement(By.tagName("h4")).getText().equals(title));
            driver.navigate().to(driver.findElement(By.xpath("/html/body/main/div/div/div[1]/div/div/div/a")).getAttribute("href"));
            Assert.assertTrue(driver.getCurrentUrl().equals(link));
            driver.navigate().back();
            driver.findElement(By.name("title")).clear();
        }
    }

    @Test
    public void SearchProject_XSS() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver","C:\\webdrivers\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();

        options.addArguments("disable-infobars");
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        String domain = "http://192.168.99.100/";
        String openSutd = domain +"projects/";
        driver.get(openSutd);

        try {
            driver.findElement(By.name("title")).sendKeys("MOMOBOT");
            driver.findElement(By.name("title")).clear();
            driver.findElement(By.name("title")).sendKeys("DEEPLEARNING-WORKSHOP-2019\"> <script>alert(\"This is not secure\")</script>");
            driver.findElement(By.xpath("/html/body/main/div/form/button")).click();
            driver.findElement(By.xpath("/html/body/main/div/div/p"));
            Assert.assertTrue(driver.findElement(By.xpath("/html/body/main/div/div/p")).getText().equals("Error! No projects are available."));
        }
        catch (Exception NoSuchElementException){
            System.out.println(NoSuchElementException);
            Assert.assertTrue(false);
        }


    }
}