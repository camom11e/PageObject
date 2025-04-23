from ..pages.main_page import Main_Page

def test_add_to_card(browser):
    who_search = "FOGGIA"
    main_page = Main_Page(browser)
    main_page.open()
    search = main_page.open_search()
    product_page = search.inputInSearch(who_search)
    formProduct = product_page.add_to_card()
    formProduct.checkProductTitle(who_search)
    product_page = formProduct.closeForm()
    
    
    
    
    