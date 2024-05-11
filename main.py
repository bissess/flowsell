import logging
import requests.exceptions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm
from api import ClientsRecordsAPI, RecordsAPI, StaffAPI, ServicesAPI, ClientsAPI
from models import Base, Records, Staff, Services, Clients

main_headers = {
    'Content-type': 'application/json',
    'Authorization': 'xbrd2ac9kgg4a9fkuyxe, User 5ca57cdfd98d4902901044f178d7de33',
    'Accept': 'application/vnd.api.v2+json'
}

# api = ClientsAPI(main_headers)
records_api = ClientsRecordsAPI(main_headers)
visits_api = RecordsAPI(main_headers)
staff_api = StaffAPI(main_headers)
services_api = ServicesAPI(main_headers)
clients_api = ClientsAPI(main_headers)

company_id = 39495
page = 1
# page_size = 200
total_count = 200

engine = create_engine('postgresql://postgres:bmwm4f82@localhost/collect_data_yclients')
Session = sessionmaker(bind=engine)


def visits_write(visits):
    Base.metadata.create_all(engine)

    with Session() as session:
        try:
            updated_visits = 0
            inserted_visits = 0

            for visit in visits:
                existing_visits = session.query(Records).filter(Records.id == str(visit['id'])).first()

                if existing_visits:
                    existing_visits.id = visit.get('id'),
                    existing_visits.company_id = visit.get('company_id'),
                    existing_visits.staff_id = visit.get('staff_id'),
                    existing_visits.date = visit.get('date'),
                    existing_visits.datetime = visit.get('datetime'),
                    existing_visits.create_date = visit.get('create_date'),
                    existing_visits.last_change_date = visit.get('last_change_date'),
                    existing_visits.comment = visit.get('comment'),
                    existing_visits.online = visit.get('online'),
                    existing_visits.confirmed = visit.get('confirmed'),
                    existing_visits.seance_length = visit.get('seance_length'),
                    existing_visits.length = visit.get('length'),
                    existing_visits.from_url = visit.get('from_url'),
                    existing_visits.visit_id = visit.get('visit_id'),
                    existing_visits.created_user_id = visit.get('created_user_id'),
                    existing_visits.deleted = visit.get('deleted'),
                    existing_visits.prepaid = visit.get('prepaid'),
                    existing_visits.prepaid_confirmed = visit.get('prepaid_confirmed'),
                    existing_visits.record_from = visit.get('record_from')
                    updated_visits += 1
                    session.commit()
                else:
                    new_visits = Records(
                        id=visit.get('id'),
                        company_id=visit.get('company_id'),
                        staff_id=visit.get('staff_id'),
                        date=visit.get('date'),
                        datetime=visit.get('datetime'),
                        create_date=visit.get('create_date'),
                        last_change_date=visit.get('last_change_date'),
                        comment=visit.get('comment'),
                        online=visit.get('online'),
                        confirmed=visit.get('confirmed'),
                        seance_length=visit.get('seance_length'),
                        length=visit.get('length'),
                        from_url=visit.get('from_url'),
                        visit_id=visit.get('visit_id'),
                        created_user_id=visit.get('created_user_id'),
                        deleted=visit.get('deleted'),
                        prepaid=visit.get('prepaid'),
                        prepaid_confirmed=visit.get('prepaid_confirmed'),
                        record_from=visit.get('record_from')
                    )

                    session.add(new_visits)
                    session.commit()
                    inserted_visits += 1

                if updated_visits:
                    total_files = len(visits)
                    tqdm.write(f'Обновлено {updated_visits} записей из {total_files}')
                else:
                    total_files = len(visits)
                    tqdm.write(f'Добавлено {inserted_visits} записей из {total_files}')

        except requests.exceptions.RequestException as e:
            logging.warning(f'Error: {e}')


# --------- GET DATA FOR STAFF TABLE ----------


def staff_write(staffs):
    Base.metadata.create_all(engine)

    with Session() as session:
        try:
            updated_staff = 0
            inserted_staff = 0

            for staff in staffs:
                existing_staffs = session.query(Staff).filter(Staff.id == str(staff['id'])).first()

                if existing_staffs:
                    existing_staffs.id = staff.get('id')
                    existing_staffs.name = staff.get('name')
                    existing_staffs.specialization = staff.get('specialization')
                    existing_staffs.avatar = staff.get('avatar')
                    existing_staffs.avatar_png = staff.get('avatar_png')
                    existing_staffs.rating = staff.get('rating')
                    existing_staffs.votes_count = staff.get('votes_count')
                    updated_staff += 1
                    session.commit()
                else:
                    new_staff = Staff(
                        id=staff.get('id'),
                        name=staff.get('name'),
                        specialization=staff.get('specialization'),
                        avatar=staff.get('avatar'),
                        avatar_png=staff.get('avatar_png'),
                        rating=staff.get('rating'),
                        votes_count=staff.get('votes_count')
                    )
                    session.add(new_staff)
                    session.commit()
                    inserted_staff += 1

        except requests.exceptions.RequestException as e:
            logging.exception(f'Except error from main.py::staff getting: {e}')


# ---------- GET DATA FOR SERVICES TABLE ------------


def services_write(services):
    Base.metadata.create_all(engine)

    with Session() as session:
        try:
            updated_services = 0
            inserted_services = 0

            for service in services:
                existing_services = session.query(Services).filter(Services.id == int(service['id'])).first()

                if existing_services:
                    existing_services.id = service.get('id')
                    existing_services.title = service.get('title')
                    existing_services.cost = service.get('cost')
                    existing_services.manual_cost = service.get('manual_cost')
                    existing_services.cost_per_unit = service.get('cost_per_unit')
                    existing_services.discount = service.get('discount')
                    existing_services.first_cost = service.get('first_cost')
                    existing_services.amount = service.get('amount')
                    updated_services += 1
                    session.commit()
                else:
                    new_services = Services(
                        id=service.get('id'),
                        title=service.get('title'),
                        cost=service.get('cost'),
                        manual_cost=service.get('manual_cost'),
                        cost_per_unit=service.get('cost_per_unit'),
                        discount=service.get('discount'),
                        first_cost=service.get('first_cost'),
                        amount=service.get('amount')
                    )
                    session.add(new_services)
                    session.commit()
                    inserted_services += 1
        except requests.exceptions.RequestException as e:
            logging.exception(f'Except error from main.py::services getting: {e}')


def write_clients(clients):
    Base.metadata.create_all(engine)

    with Session() as session:
        try:
            updated_clients = 0
            inserted_clients = 0

            for client in clients:
                existing_clients = session.query(Clients).filter(Clients.id == int(client['id'])).first()

                if existing_clients:
                    existing_clients.id = client.get('id')
                    existing_clients.name = client.get('name')
                    existing_clients.surname = client.get('surname')
                    existing_clients.patronymic = client.get('patronymic')
                    existing_clients.display_name = client.get('display_name')
                    existing_clients.phone = client.get('phone')
                    existing_clients.card = client.get('card')
                    existing_clients.email = client.get('email')
                    existing_clients.success_visits_count = client.get('success_visits_count')
                    existing_clients.fail_visits_count = client.get('fail_visits_count')
                    existing_clients.discount = client.get('discount')
                    existing_clients.is_new = client.get('is_new')
                    existing_clients.custom_fields = client.get('custom_fields')
                    updated_clients += 1
                    session.commit()
                else:
                    new_clients = Clients(
                        id=client.get('id'),
                        name=client.get('name'),
                        surname=client.get('surname'),
                        patronymic=client.get('patronymic'),
                        display_name=client.get('display_name'),
                        phone=client.get('phone'),
                        card=client.get('card'),
                        email=client.get('email'),
                        success_visits_count=client.get('success_visits_count'),
                        fail_visits_count=client.get('fail_visits_count'),
                        discount=client.get('discount'),
                        is_new=client.get('is_new'),
                        custom_fields=client.get('custom_fields')
                    )
                    session.add(new_clients)
                    session.commit()
                    inserted_clients += 1

        except requests.exceptions.RequestException as e:
            logging.exception(f'Except error from getting of clients data: {e}')


working = True
while working:

    # clients = api.get_clients(company_id, page, page_size)
    visits = visits_api.get_list_of_visits(company_id, page, total_count)
    staffs = staff_api.get_staff_info(company_id, page, total_count)
    services = services_api.get_list_of_services(company_id, page, total_count)
    clients = clients_api.get_list_of_clients(company_id, page, total_count)

    if visits:
        page += 1

        visits_write(visits)
        staff_write(staffs)
        services_write(services)
        write_clients(clients)

    else:
        working = False

