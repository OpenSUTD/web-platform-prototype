package OpenSUTD;

import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import java.util.List;

public class Test_OpenSUTD_Approval {
    @Test
    public void Reject_Projects(){
        System.setProperty("webdriver.chrome.driver","C:\\webdrivers\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();

        options.addArguments("disable-infobars");
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        String domain = "http://192.168.99.100/";
        String openSutd = domain +"admin/approval";
        driver.get(openSutd);

        Assert.assertTrue(driver.getCurrentUrl().equals(domain + "accounts/login/?next=/admin/approval"));

        String myUserName = "superadmin";
        String myPassword = "asdf1234";

        // get the user name field of the account page
        driver.findElement(By.name("login")).sendKeys(myUserName);
        driver.findElement(By.name("password")).sendKeys(myPassword);

        driver.findElement(By.className("primaryAction")).click();

        Assert.assertTrue(driver.getCurrentUrl().equals(openSutd));

        List<WebElement> pendTitlesList = driver.findElements(By.className("pending-project-title"));

        String[] pendTitles = new String[pendTitlesList.size()];

        for (int i = 0; i < pendTitlesList.size(); i=i+1) {
            pendTitles[i] = pendTitlesList.get(i).getText();
        }

        if(pendTitlesList.size() == driver.findElements(By.className("button-reject-pending")).size()){
            for(int i=0; i<pendTitlesList.size(); i++){
                driver.findElement(By.xpath("/html/body/main/div/div/div[1]/div[1]/div/div/div[1]/div[2]/form/button")).click();
            }
        }

        List<WebElement> rejcTitlesList = driver.findElements(By.className("rejected-project-title"));

        String[] rejcTitles = new String[rejcTitlesList.size()];

        for (int i = 0; i < rejcTitlesList.size(); i=i+1) {
            rejcTitles[i] = rejcTitlesList.get(i).getText();
        }

        for (String pendTitle: pendTitles) {
            int flag = 0;
            for(int i=0; i < rejcTitles.length ;i++)
            {
                if(rejcTitles[i].equals(pendTitle))
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0){
                Assert.assertTrue(false);
            }
        }
        Assert.assertTrue(true);
    }

    @Test
    public void Pending_Approval(){
        System.setProperty("webdriver.chrome.driver","C:\\webdrivers\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();

        options.addArguments("disable-infobars");
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        String domain = "http://192.168.99.100/";
        String openSutd = domain +"admin/approval";
        driver.get(openSutd);

        Assert.assertTrue(driver.getCurrentUrl().equals(domain + "accounts/login/?next=/admin/approval"));

        String myUserName = "superadmin";
        String myPassword = "asdf1234";

        // get the user name field of the account page
        driver.findElement(By.name("login")).sendKeys(myUserName);
        driver.findElement(By.name("password")).sendKeys(myPassword);

        driver.findElement(By.className("primaryAction")).click();

        Assert.assertTrue(driver.getCurrentUrl().equals(openSutd));

        List<WebElement> pendTitlesList = driver.findElements(By.className("pending-project-title"));

        String[] pendTitles = new String[pendTitlesList.size()];

        for (int i = 0; i < pendTitlesList.size(); i=i+1) {
            pendTitles[i] = pendTitlesList.get(i).getText();
        }

        if(pendTitlesList.size() == driver.findElements(By.className("button-accept-pending")).size()){
            for(int i=0; i<pendTitlesList.size(); i++){
                driver.findElement(By.xpath("/html/body/main/div/div/div[1]/div[1]/div/div/div[1]/div[1]/form/button")).click();
            }
        }

        driver.navigate().to(domain + "projects/");

        List<WebElement> projectTitlesList = driver.findElements(By.tagName("h4"));

        String[] projTitles = new String[projectTitlesList.size()];

        for (int i = 0; i < projectTitlesList.size(); i=i+1) {
            projTitles[i] = projectTitlesList.get(i).getText();
        }

        for (String pendTitle: pendTitles) {
            int flag = 0;
            for(int i=0; i < projTitles.length ;i++)
            {
                if(projTitles[i].equals(pendTitle))
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0){
                Assert.assertTrue(false);
            }
        }
        Assert.assertTrue(true);
    }

    @Test
    public void Rejected_Approval(){
        System.setProperty("webdriver.chrome.driver","C:\\webdrivers\\chromedriver.exe");

        ChromeOptions options = new ChromeOptions();

        options.addArguments("disable-infobars");
        options.addArguments("--start-maximized");

        WebDriver driver = new ChromeDriver(options);

        String domain = "http://192.168.99.100/";
        String openSutd = domain +"admin/approval";
        driver.get(openSutd);

        Assert.assertTrue(driver.getCurrentUrl().equals(domain + "accounts/login/?next=/admin/approval"));

        String myUserName = "superadmin";
        String myPassword = "asdf1234";

        // get the user name field of the account page
        driver.findElement(By.name("login")).sendKeys(myUserName);
        driver.findElement(By.name("password")).sendKeys(myPassword);

        driver.findElement(By.className("primaryAction")).click();

        Assert.assertTrue(driver.getCurrentUrl().equals(openSutd));

        List<WebElement> pendTitlesList = driver.findElements(By.className("rejected-project-title"));

        String[] pendTitles = new String[pendTitlesList.size()];

        for (int i = 0; i < pendTitlesList.size(); i=i+1) {
            pendTitles[i] = pendTitlesList.get(i).getText();
        }

        if(pendTitlesList.size() == driver.findElements(By.className("button-accept-reject")).size()){
            for(int i=0; i<pendTitlesList.size(); i++){
                driver.findElement(By.xpath("/html/body/main/div/div/div[2]/div[1]/div/div/div[1]/div[1]/form/button")).click();
            }
        }

        driver.navigate().to(domain + "projects/");

        List<WebElement> projectTitlesList = driver.findElements(By.tagName("h4"));

        String[] projTitles = new String[projectTitlesList.size()];

        for (int i = 0; i < projectTitlesList.size(); i=i+1) {
            projTitles[i] = projectTitlesList.get(i).getText();
        }

        for (String pendTitle: pendTitles) {
            int flag = 0;
            for(int i=0; i < projTitles.length ;i++)
            {
                if(projTitles[i].equals(pendTitle))
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0){
                Assert.assertTrue(false);
            }
        }
        Assert.assertTrue(true);
    }
}
