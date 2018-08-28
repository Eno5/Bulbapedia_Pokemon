import pandas as pd
from selenium import webdriver

#import Pokemon Names and Types
names = pd.read_csv('Pokemon List.csv')
print(names.head())

#initialize browser
driver = webdriver.Firefox()
driver.minimize_window()
driver.get('https://bulbapedia.bulbagarden.net/wiki/Abomasnow_(Pok%C3%A9mon)')

"""EXPLORATORY"""

exp = []

try:
    for pokemon in names.iloc[:,2]:
        try:
            driver.get('https://bulbapedia.bulbagarden.net/wiki/'+pokemon+'_(Pok%C3%A9mon)')
        except:
            continue

        cat = driver.find_element_by_xpath('//a[@title="Pokémon category"]/span').text
        pic = driver.find_element_by_xpath('//img[@width="250"]').get_attribute('src')

        ability = driver.find_element_by_xpath('//span[contains(., "Abili")]/ancestor::b/following-sibling::table/tbody/tr/td').text

        hid_ability = driver.find_elements_by_xpath('//small[contains(., "Hidden")]/preceding-sibling::a')[0].get_attribute('title')
        gender = driver.find_element_by_xpath('//span[contains(., "Gender")]/ancestor::b/following-sibling::table').text
        catch = driver.find_element_by_xpath('//span[contains(., "Catch")]/ancestor::b/following-sibling::table').text

        egg_groups = driver.find_element_by_xpath('//span[contains(., "Egg")]/ancestor::b/following-sibling::table').text
        hatch_time = driver.find_element_by_xpath('//span[contains(., "Hatch")]/ancestor::b/following-sibling::table').text

        height = driver.find_element_by_xpath('//span[text()="Height"]/ancestor::b/following-sibling::table').text
        weight = driver.find_element_by_xpath('//span[text()="Weight"]/ancestor::b/following-sibling::table').text
        friend = driver.find_element_by_xpath('//span[contains(., "endship")]/ancestor::b/following-sibling::table').text

        locations = driver.find_element_by_xpath('//span[@id="Game_locations"]/parent::*/following-sibling::table').text

        HP = driver.find_element_by_xpath('//span[text()="HP"]/ancestor::tr/ancestor::tr').text
        ATK = driver.find_element_by_xpath('//span[text()="Attack"]/ancestor::tr/ancestor::tr').text
        DEF = driver.find_element_by_xpath('//span[text()="Defense"]/ancestor::tr/ancestor::tr').text
        Sp_ATK = driver.find_element_by_xpath('//span[text()="Sp.Atk"]/ancestor::tr/ancestor::tr').text
        Sp_DEF = driver.find_element_by_xpath('//span[text()="Sp.Def"]/ancestor::tr/ancestor::tr').text
        SPD = driver.find_element_by_xpath('//span[text()="Speed"]/ancestor::tr/ancestor::tr').text

        norm_DMG = driver.find_elements_by_xpath('//span[@id="Type_effectiveness"]/parent::*/following-sibling::table[1]/tbody/tr')[1].text
        weak_DMG = driver.find_elements_by_xpath('//span[@id="Type_effectiveness"]/parent::*/following-sibling::table[1]/tbody/tr')[2].text
        immune_DMG = driver.find_elements_by_xpath('//span[@id="Type_effectiveness"]/parent::*/following-sibling::table[1]/tbody/tr')[3].text
        resist_DMG = driver.find_elements_by_xpath('//span[@id="Type_effectiveness"]/parent::*/following-sibling::table[1]/tbody/tr')[4].text

        try:
            evo = driver.find_element_by_xpath('//span[@id="Evolution"]/parent::*/following-sibling::table[1]').text
        except:
            evo = ''

        exp.append([cat, pic, ability, hid_ability, catch, egg_groups, hatch_time, height, weight, friend, locations,
                    HP, ATK, DEF, Sp_ATK, Sp_DEF, SPD, norm_DMG, weak_DMG, immune_DMG, resist_DMG, evo])
except:
    print("Error")

driver.close()
#print(pic)

df = pd.DataFrame(exp)

df.to_csv('Explore.csv')