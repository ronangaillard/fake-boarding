#!/usr/local/bin/python
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import treepoem
from datetime import date, datetime


def generer_barcode(data):
    image = treepoem.generate_barcode('azteccode', data ,{})
    image.save('static/aztec-code.png')
    image = treepoem.generate_barcode('pdf417', data ,{})
    image.save('static/pdf417-code.png')

def resize_str(string, size):
    return string[0:size].ljust(size)

def generer_payload(passenger_lastname, passenger_firstname, booking_reference, from_airport, to_airport, carrier, flight_number, flight_date, seat_number, seat_row, passenger_status,check_in_nb, flight_class = 'F', extra_data = False):
    payload = 'M'
    payload += '1'
    small_name = passenger_lastname + '/' + passenger_firstname
    small_name = resize_str(small_name, 20)
    payload += small_name
    payload += 'E'
    payload += resize_str(str(booking_reference), 6) + ' '
    payload += resize_str(from_airport, 3)
    payload += resize_str(to_airport, 3)
    payload += resize_str(carrier, 2) + ' '
    payload += str(flight_number).zfill(4) + ' '
    first_day = date(flight_date.year, 1, 1)
    delta = flight_date - first_day
    payload += str(delta.days).zfill(3)
    payload += flight_class #classe
    payload += str(seat_number).zfill(3) + seat_row
    payload += check_in_nb.zfill(4) + ' '
    payload += str(passenger_status)
    if not extra_data:
        payload += '00'
    return payload


# Config
PORT = 3000

# Creates the application
app = Flask(__name__)
app.config.from_object(__name__)

app.debug = True

#D
# Routes

@app.route('/')
def render_index():
    return render_template('index.html')



@app.route('/generatecode', methods=['POST'])
def generate_code():
    flight_date =  datetime.strptime(request.form['flight-date'], '%d/%m/%Y').date()

    pl = generer_payload(request.form['last-name'], request.form['first-name'], request.form['booking-reference'], request.form['from-airport'], request.form['to-airport'], request.form['carrier'], request.form['flight-number'], flight_date, request.form['seat-number'],request.form['seat-row'],request.form['passenger-status'],request.form['check-in-number'])

    generer_barcode(pl)
    return render_template('view_code.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=PORT)
