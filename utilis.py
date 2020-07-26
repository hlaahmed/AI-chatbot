import app


def getPhone(phone):
    if app.db.session.query(app.Users).filter(app.Users.phone == phone).count() == 0:
        return 0
    else:
        return 1


def save(name, phone, company, service):
    if(str(company)=="etisalate"):
        phone = int(str("011") + str(phone))
    elif(str(company)=="orange"):
        phone = int(str("012") + str(phone))
    else:
        phone = int(str("010") + str(phone))
    data = app.Users(str(name), phone, str(company), str(service))
    app.db.session.add(data)
    app.db.session.commit()
