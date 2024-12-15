class Cart():
    def __init__(self, request):
        
        self.session = request.session

        # Returning user - obtain his/her existing session
        cart = self.session.get('session_key')

        # New user - generate a new session
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product, product_quantity):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] = product_quantity

        else:
            self.cart[product_id] = {'price': str(product.price), 'quantity': product_quantity}
            
        self.session.modified = True

    def save(self):
        self.session.modified = True