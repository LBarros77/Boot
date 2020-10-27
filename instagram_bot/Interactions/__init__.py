from selenium.webdriver.common.keys import Keys
import random
from time import sleep
from packages import DB

def writed(word, text_box):
    for latter in word:
        text_box.send_keys(latter)
        sleep(random.randint(1, 4))

def getHrefs(self, explore, commentadors=False, adress=True):
    driver = self.driver
    if adress:
        driver.get(f"https://www.instagram.com/{explore}/")
    for i in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(random.randint(i, 5))
    sleep(random.randint(2, 6))
    hrefs = driver.find_elements_by_tag_name("a")
    hrefs_list = [elem.get_attribute("href") for elem in hrefs]
    total = len(hrefs_list)
    random.shuffle(hrefs_list)
    link_list = []
    if commentadors:
        cont = 2
    else:
        try:
            cont = random.randint(5, 20)
        except Exception as e:
            print("\033[31mErro em limitador cont\033[m ", e)
    print(f"De {total} referências {cont} serão executadas")
    for link in hrefs_list:
        try:
            if link.index("/p/") != -1:
                link_list.append(link)
                cont -= 1
        except:
            pass
        if cont == 0:
            break
    return link_list

def like_comment(self, writer, hashtag):
        driver = self.driver
        if hashtag:
            ht = DB.hashtag_list(self.username)
            driver.find_element_by_css_selector(".TqC_a").click()
            tag_box = driver.find_element_by_css_selector(".TqC_a")
            writed(f"#{ht}", tag_box)
            tag_box.send_keys(Keys.RETURN)
        else:
            driver.find_element_by_xpath("//a[@href='/explore/']").click()
        sleep(random.randint(3, 9))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        hrefs_list = [elem.get_attribute("href") for elem in hrefs]
        print(f"Foram encontradas {len(hrefs_list)} referências")
        post_list = []
        random.shuffle(hrefs_list)
        cont = 2
        for href in hrefs_list:
            try:
                if href.index("/p/") != -1:
                    post_list.append(href)
                    cont -= 1
            except:
                pass
            if cont == 0:
                break
        print(f"Foram selecionadas {len(post_list)} postagens")
        for href in post_list:
            driver.get(href)
            sleep(random.randint(3, 8))
            try:
                driver.find_element_by_css_selector(".fr66n").click()
                if writer:
                    driver.find_element_by_css_selector("._15y0l").click()
                    text_box = driver.find_element_by_css_selector(".Ypffh")
                    writed(DB.comment_list(self.username), text_box)
                    text_box.end_keys(Keys.RETURN)
            except Exception as e:
                print(e)

def like_comment_commentadors(self, write, hashtag):
    driver = self.driver
    if hashtag:
        ht = DB.hashtag_list(self.username)
        driver.get(f"https://www.instagram.com/explore/tags/{ht}/")
    else:
        driver.find_element_by_expath("//a[@href='/explore/']").click()
    sleep(random.randint(3, 8))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    hrefs = driver.find_elements_by_tag_name("a")
    hrefs_list = [elem.get_attribute("href") for elem in hrefs]
    print(f"Foram encontradas {len(hrefs_list)} referẽncias")
    random.shuffle(hrefs_list)
    link_list = []
    cont = 2
    for link in hrefs_list:
        try:
            if link.index("/p/") != -1:
                link_list.append(link)
                cont -= 1
        except:
            pass
        if cont == 0:
            break
    for n, link in enumerate(link_list):
        driver.get(link)
        hrefs_list.clear()
        sleep(random.randint(3, 6))
        try:
            peoples = driver.find_elements_by_css_selector(".yWX7d")
            href_peoples = [elem.get_attribute("href") for elem in peoples]
            for href in href_peoples:
                try:
                    auxiliar = href[26:]
                    if auxiliar not in hrefs_list:
                        hrefs_list.append(auxiliar)
                except:
                    pass
        except Exception as e:
            print(e)
        print(f"Na {n+1}º postagem tem {len(hrefs_list)} comentários")
        for userx in hrefs_list:
            driver.get(f"https://www.instagram.com/{userx}")
            sleep(random.randint(3, 8))
            hrefs = driver.find_elements_by_tag_name("a")
            post_list = [elem.get_attribute("href") for elem in hrefs]
            random.shuffle(post_list)
            cont = 2
            link_post = []
            for post in post_list:
                try:
                    if post.index("/p/") != -1:
                        link_post.append(post)
                        cont -= 1
                except:
                    pass
                if cont == 0:
                    break
            for post in link_post:
                driver.get(post)
                sleep(random.randint(3, 8))
                try:
                    driver.find_element_by_css_selector(".fr66n").click()
                    sleep(random.randint(2, 5))
                    if write:
                        driver.find_element_by_css_selector("._15y0l").click()
                        text_box = driver.find_element_by_css_selector(".Ypffh")
                        writed(DB.comment_list(self.username), text_box)
                        text_box.send_keys(Keys.RETURN)
                except Exception as e:
                    print(f"\033[31mErro em postagem de p/ativo\033[m {e}")

def like_comment_automatic(self):
    location = random.choice([True, False])
    hashtag = random.choice([True, False])
    commentadors = random.choice([True, False])
    driver = self.driver
    if hashtag:
        ht = DB.hashtag_list(self.username)
        link_list = getHrefs(self, f"explore/tags/{ht}", commentadors)
    elif location:
        driver.get(f"https://www.instagram.com/{self.username}/")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(random.randint(1, 4))
        hrefs = driver.find_elements_by_tag_name("a")
        hrefs_list = [elem.get_attribute("href") for elem in hrefs]
        post_link = []
        for link in hrefs_list:
            try:
                if link.index("/p/") != -1:
                    post_link.append(link)
            except:
                pass
        random.shuffle(post_link)
        for link in post_link:
            driver.get(link)
            sleep(random.randint(1, 5))
            try:
                driver.find_element_by_css_selector(".O4GlU").click()
                link_list = getHrefs(self, commentadors, adress=False)
                break
            except Exception as e:
                print(e)
    else:
        driver.find_element_by_expath("//a[@href='/explore/']").click()
        link_list = getHrefs(self, commentadors, adress=False)
    for link in link_list:
        driver.get(link)
        sleep(random.randint(2, 5))
        if commentadors == False:
            try:
                driver.find_element_by_css_selector(".fr66n").click()
                comment = random.choice([True, False])
                if comment:
                    driver.find_element_by_css_selector("._15y0l").click()
                    sleep(1)
                    driver.find_element_by_css_selector(".Ypffh").click()
                    text_box = driver.find_element_by_css_selector(".Ypffh")
                    writed(DB.comment_list(self.username), text_box)
                    text_box.send_keys(Keys.RETURN)
            except Exception as e:
                print(e)
        else:
            hrefs = driver.find_elements_by_css_selector(".yWX7d._8A5w5.ZIAjV")
            hrefs_list = [elem.get_attribute("href") for elem in hrefs]
            perfis_list = []
            cont = 3
            for href in hrefs_list:
                href = href[26:]
                if href not in perfis_list:
                    perfis_list.append(href)
                    cont -= 1
                if cont == 0:
                    break
            random.shuffle(perfis_list)
            for href in perfis_list:
                driver.get(f"https://www.instagram.com/{href}")
                sleep(random.randint(3, 6))
                hrefs = driver.find_elements_by_tag_name("a")
                hrefs_list = [elem.get_attribute("href") for  elem in hrefs]
                random.shuffle(hrefs_list)
                cont = 2
                link_list = []
                for post in hrefs_list:
                    try:
                        if post.index("/p/") != -1:
                            link_list.append(post)
                            cont -= 1
                    except:
                        pass
                    if cont == 0:
                        break
                for post in link_list:
                    driver.get(post)
                    sleep(random.randint(3, 7))
                    try:
                        driver.find_element_by_css_selector(".fr66n").click()
                        comment = random.choice([True, False])
                        if comment:
                            driver.find_element_by_css_selector("._15y0l").click()
                            text_box = driver.find_element_by_css_selector(".Ypffh")
                            writed(DB.comment_list(self.username), text_box)
                            text_box.send_keys(Keys.RETURN)
                        sleep(random.randint(3, 7))
                    except Exception as e:
                        print(e)
