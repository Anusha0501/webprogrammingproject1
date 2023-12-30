from flask import Flask,render_template,request,redirect
import psycopg2

app = Flask(__name__)

@app.route("/")
def move():
    return redirect('login')


@app.route("/home")
def home():
    conn = psycopg2.connect(database='postgres',
                                user='postgres',
                                password='anant15052004',
                                host='localhost',
                                port=5432)
    cur=conn.cursor()
    cur.execute('select * from products order by product_id;')
    product_data=cur.fetchall()
    conn.close()
    
    return render_template('amazon.html',product_data=product_data)

@app.route("/orders", methods=["GET", "POST"])
def orders():
    conn = psycopg2.connect(database='postgres',
                                user='postgres',
                                password='anant15052004',
                                host='localhost',
                                port=5432)
    cur=conn.cursor()
    if request.method == 'POST':
        name = request.form['search']  # Update to match the input name in your form
        # Assuming you have a valid database connection and cursor here
        cur.execute(f"SELECT product_image, product_name, product_description FROM products WHERE product_name LIKE '%%{name}%%';")
        data = cur.fetchall()

        return render_template('orders.html', data=data)
    else:
        return render_template('orders.html', data=None)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/return_orders')
def return_orders():
    return render_template('return_orders.html')

@app.route('/create_account')
def create_account():
    return render_template('account.html');


if __name__=='__main__':
    app.run(debug=True)
