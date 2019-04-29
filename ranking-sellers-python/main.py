from operator import itemgetter

class SellersRancking:

    def sorted_list(self, sellers, reversed=True):
        """Sorted method
        
        Arguments:
            sellers {list of dictionaries}
        
        Keyword Arguments:
            reversed {bool} -- Order by list (default: {True})
        
        Returns:
            list -- Ordered list
        """
        return sorted(sellers, key=itemgetter('value'), reverse=reversed)

    def best_seller(self, sellers):
        """Show seller with highest sales value
        
        Arguments:
            sellers {list of dictionaries}
        
        Returns:
            list -- Best seller
        """
        try:
            return [self.sorted_list(sellers)[0]['name']]
        except Exception:
            return []

    def rancking_list(self, sellers):
        """List all sellers ordered by value sold, from highest to lowest
        
        Arguments:
            sellers {list of dictionaries}
        
        Returns:
            list -- Sellers list
        """
        try:
            return [sellers['name'] for sellers in self.sorted_list(sellers)]
        except Exception:
            return []

    def best_seller_store(self, sellers, store):
        """Show best seller of a store
        
        Arguments:
            sellers {list of dictionaries}
            store {int} -- store number
        
        Returns:
            list -- Best seller of a store
        """
        try:
            return [([sellers['name'] for sellers in self.sorted_list(sellers) \
                if sellers['store'] == store])[0]]
        except Exception:
            return []

    def sales_goals(self, sellers):
        """List of sellers who did not hit the goal
        
        Arguments:
            sellers {list of dictionaries}
        
        Returns:
            list -- Sellers list
        """
        try:
            return [sellers['name'] for sellers in self.sorted_list(sellers, False) \
                if sellers['value'] < 500]
        except Exception:
            return []