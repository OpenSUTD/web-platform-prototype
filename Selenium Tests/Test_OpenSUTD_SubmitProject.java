package OpenSUTD;

import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.util.Random;

public class Test_OpenSUTD_SubmitProject {

    @Test
    public void SubmitPage_WithoutLogin(){
        System.setProperty("webdriver.chrome.driver","C:\\webdrivers\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();

        options.addArguments("disable-infobars");
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        String domain = "http://192.168.99.100/";
        String openSutd = domain +"admin/submit";
        driver.get(openSutd);

        String myUserName = "superadmin";
        String myPassword = "asdf1234";

        Assert.assertTrue(driver.getCurrentUrl().equals(domain + "accounts/login/?next=/admin/submit"));

        // get the user name field of the account page
        driver.findElement(By.name("login")).sendKeys(myUserName);
        driver.findElement(By.name("password")).sendKeys(myPassword);

        driver.findElement(By.className("primaryAction")).click();

        Assert.assertTrue(driver.getCurrentUrl().equals(openSutd));
    }


    @Test
    public void SubmitProject(){
        System.setProperty("webdriver.chrome.driver","C:\\webdrivers\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();

        options.addArguments("disable-infobars");
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        String domain = "http://192.168.99.100/";
        String openSutd = domain +"admin/submit";
        driver.get(openSutd);

        Assert.assertTrue(driver.getCurrentUrl().equals(domain + "accounts/login/?next=/admin/submit"));

        String myUserName = "superadmin";
        String myPassword = "asdf1234";

        // get the user name field of the account page
        driver.findElement(By.name("login")).sendKeys(myUserName);
        driver.findElement(By.name("password")).sendKeys(myPassword);

        driver.findElement(By.className("primaryAction")).click();

        Assert.assertTrue(driver.getCurrentUrl().equals(openSutd));

        Random random = new Random();

        int count = random.nextInt(8);

        for(int i = 0; i <= count; i++) {
            driver.findElement(By.name("project_name")).sendKeys("Project" + random.nextInt(10000));
            driver.findElement(By.name("caption")).sendKeys("Test projects for Selenium test cases");
            driver.findElement(By.xpath("//*[@id=\"id_category_" + random.nextInt(5) + "\"]")).click();
            driver.findElement(By.name("featured_image")).sendKeys("https://media1.giphy.com/media/7MZ0v9KynmiSA/giphy.gif");
            driver.findElement(By.name("github_url")).sendKeys("https://github.com/" + random.nextInt(10000));
            driver.findElement(By.name("poster_url")).sendKeys("https://media1.giphy.com/media/7MZ0v9KynmiSA/giphy.gif");
            driver.findElement(By.xpath("/html/body/main/div/form/input[2]")).click();
            if(i==count){
                break;
            }
            driver.navigate().back();
            driver.findElement(By.name("project_name")).clear();
            driver.findElement(By.name("caption")).clear();
            driver.findElement(By.name("featured_image")).clear();
            driver.findElement(By.name("github_url")).clear();
            driver.findElement(By.name("poster_url")).clear();
        }

        Assert.assertTrue(driver.getCurrentUrl().equals(domain + "admin/approval"));
    }
}
