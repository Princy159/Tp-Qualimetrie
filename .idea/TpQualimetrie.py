from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time  # Importer le module time

# Initialisation du navigateur Firefox
driver = webdriver.Firefox()
driver.get("https://www.zalando.fr/")

# Recherche de l'élément de la barre de recherche et saisie de "montre"
barreDeRecherche = driver.find_element(By.NAME, "q")
barreDeRecherche.send_keys("montre")
barreDeRecherche.send_keys(Keys.RETURN)

# Attendre que la page se charge
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//div[@class='_5qdMrS w8MdNG cYylcv BaerYO _75qWlu iOzucJ JT3_zV _Qe9k6'])[3]"))
)

# Cliquer sur le premier résultat
clickPremier = driver.find_element(By.XPATH, "(//div[@class='_5qdMrS w8MdNG cYylcv BaerYO _75qWlu iOzucJ JT3_zV _Qe9k6'])[3]")
clickPremier.click()

# Attendre que la page se charge
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='_ZDS_REF_SCOPE_ vfoVrE DJxzzA u9KIT8 uEg2FS U_OhzR ZkIJC- Vn-7c- VWL_Ot _13ipK_ FCIprz heWLCX lXdmf0 LyRfpJ Md_Vex NN8L-8 EmWJce EvwuKo gcK-9K EKabf7 aX2-iv r9BRio pOsi7r mo6ZnF  Wy3rmK']/span[text()='Ajouter au panier']"))
)

# Ajouter au panier
ajoutPanier = driver.find_element(By.XPATH, "//button[@class='_ZDS_REF_SCOPE_ vfoVrE DJxzzA u9KIT8 uEg2FS U_OhzR ZkIJC- Vn-7c- VWL_Ot _13ipK_ FCIprz heWLCX lXdmf0 LyRfpJ Md_Vex NN8L-8 EmWJce EvwuKo gcK-9K EKabf7 aX2-iv r9BRio pOsi7r mo6ZnF  Wy3rmK']/span[text()='Ajouter au panier']")
ajoutPanier.click()

# Attendre que le panier se charge
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//div[@class='egPhqr CIcWFg n4kyHD e5GQII _9bYLON z-navicat-header_navToolItem-bag'])"))
)

# Cliquer sur le panier
clickPanier = driver.find_element(By.XPATH, "(//div[@class='egPhqr CIcWFg n4kyHD e5GQII _9bYLON z-navicat-header_navToolItem-bag'])")
clickPanier.click()

# Attendre que la page du panier se charge
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//select[@class='z-2-dropdown__control']"))
)

# Cliquer sur le sélecteur de quantité pour ouvrir la liste déroulante
select_quantite = driver.find_element(By.XPATH, "//select[@class='z-2-dropdown__control']")
select_quantite.click()

# Attendre que la liste déroulante se charge
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//option[@value='4']"))
)

# Sélectionner la quantité  dans le menu déroulant
select_quantite_option = driver.find_element(By.XPATH, "//option[@value='4']")
select_quantite_option.click()

# Attendre que le bouton "Commander" soit visible et cliquer dessus
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[@class='z-1-button z-coast-base-primary-accessible z-coast-base__totals-tile__button-checkout z-1-button--primary z-1-button--button']/div[text()='Commander']"))
)
commander_button = driver.find_element(By.XPATH, "//button[@class='z-1-button z-coast-base-primary-accessible z-coast-base__totals-tile__button-checkout z-1-button--primary z-1-button--button']/div[text()='Commander']")
commander_button.click()


time.sleep(20)


driver.save_screenshot('capture_ecran_commande.png')
time.sleep(20)

driver.quit()
