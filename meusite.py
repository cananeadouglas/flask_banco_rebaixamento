from crypt import methods
from flask import Flask, render_template, request, redirect, url_for, flash, g, Response
import sqlite3
from random import randint
import math, datetime, time
# import flask_sqlalchemy

app = Flask(__name__)

DB_URL = "employee.db"

@app.route('/')
def index():
    variavel = "Você esta programando em Python Flask"
    return render_template("index.html", variavel_base = variavel)

@app.before_request
def before_request():
    print("Conectando ao banco")
    conn = sqlite3.connect(DB_URL)
    g.conn = conn

@app.teardown_request
def after_request(exception):
    if g.conn is not None:
        g.conn.close()
        print("desconectando ao banco")

#conection bank - conexão banco
@app.route('/banco')
def banco():
    return render_template("banco.html")

@app.route('/savedetails', methods = ["POST", "GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            address = request.form["address"]  
            with sqlite3.connect("employee.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Employees (name, email, address) values (?,?,?)",(name,email,address))
                con.commit()  
                msg = "Employee successfully Added"  
        except:
            con.rollback()
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("success.html", msg = msg)  
            con.close()

@app.route('/delete')  
def delete():  
    return render_template("delete.html")  

@app.route('/deleterecord', methods=["POST", "GET"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("employee.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from Employees where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record.html", msg = msg)

app.route('/view', methods=["POST", "GET"])  
def view():
    try:
        if request.method == "GET":
            msg = "oi"
            return render_template("success.html", msg = msg)
        else:
            query = """SELECT * FROM Employees;"""
            cursor = g.conn.execute(query)
            dados_dic = cursor.fetchall()
            return render_template("view.html", rows = dados_dic)  
    except:
        msg = "não deu"
        return render_template("success.html", msg = msg)
    

@app.route('/add', methods=["POST", "GET"])  
def add():  
    return render_template("add.html")

if __name__ == "__main__":  
    app.run(debug = True)


@app.route('/rebaixamento', methods = ["POST", "GET"])
def rebaixamento():
    if request.method == "POST":
        qtd_m_palestes = int(request.form["caminhao"])
        qtd_m_lastro = int(request.form["lastro"])
        qtd_m_empilhamento = int(request.form["empilhamento"])
        compra = int(request.form["compra"])
        
        qtd_m_caixa_por_palete = qtd_m_lastro * qtd_m_empilhamento
            #print(" ")
            #print("a quantidade máxima de caixas por palete é (", qtd_m_caixa_por_palete, ")")
            #teste = input("Você confirma? digite y para sim e n para não ")
            #print(" ")

        menos_1_lastro = qtd_m_empilhamento-1
        menos_2_lastro = qtd_m_empilhamento-2
        menos_3_lastro = qtd_m_empilhamento-3
            #print(menos_1_lastro, menos_2_lastro, menos_3_lastro)
            #print("continuar")
        
            #print(" ")

        caixa_palete_ideal = qtd_m_caixa_por_palete - qtd_m_lastro
            #print("A quantidade de CAIXAS passou a ser: ", caixa_palete_ideal)

        total_caixas_compradas = compra * qtd_m_caixa_por_palete
            #print( "A quantidade Total de CAIXAS é de: ", total_caixas_compradas)

        qtd_lastro_maximo_ideal = total_caixas_compradas / qtd_m_lastro
            #print( 'O total de lastros é {}'.format(math.trunc(qtd_lastro_maximo_ideal)) )

        information01 = qtd_lastro_maximo_ideal / menos_1_lastro
        information02 = qtd_lastro_maximo_ideal / menos_2_lastro
        information03 = qtd_lastro_maximo_ideal / menos_3_lastro

            #print(information01, information02, information03)

        maior = 0
        menor = information01
        if information02 < information01 and information02 < information03:
            menor = information02
        if information03 < information01 and information03 < information02:
            menor = information03
            maior = information01
        if information02 > information01 and information02 > information03:
            maior = information02
        if information03 > information01 and information03 > information02:
            maior = information03

                #print('o maior é {} e o menor é {}'.format(maior, menor))

        if menor > qtd_m_palestes:
            msg = "oi"
                #print("nada fazer")
        if menor <= qtd_m_palestes:
            numero_de_caixas_ideal = caixa_palete_ideal * int('{}'.format(math.trunc(menor)))
                #print(numero_de_caixas_ideal)
                # fim do programa
            saldo = total_caixas_compradas - numero_de_caixas_ideal
            resultado = "A quantidade total de paletes passou a ser: {} sendo que são {} paletes inteiros com {} caixas e 1 palete com {} caixas".format(int('{}'.format(math.trunc(menor+1))), math.trunc(menor), caixa_palete_ideal, saldo)
                
            return render_template("base.html", msg = resultado)
    
    else:
        nada = "não deu"
        return render_template("rebaixamento.html", msg = nada)