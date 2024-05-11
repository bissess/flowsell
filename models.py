from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, LargeBinary, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


# class Client(Base):
#     __tablename__ = 'altegio_clients'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     phone = Column(String)
#     email = Column(String)
#     discount = Column(Integer)
#     first_visit_date = Column(Date)
#     last_visit_date = Column(Date)
#     sold_amount = Column(Integer)
#     visit_count = Column(Integer)


class Records(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    staff_id = Column(Integer, ForeignKey('staff.id'))
    date = Column(Date)
    datetime = Column(DateTime)
    create_date = Column(Date)
    last_change_date = Column(DateTime)
    comment = Column(String)
    online = Column(String)
    confirmed = Column(Integer)
    seance_length = Column(Integer)
    length = Column(Integer)
    from_url = Column(String)
    visit_id = Column(Integer)
    created_user_id = Column(Integer)
    deleted = Column(String)
    prepaid = Column(String)
    prepaid_confirmed = Column(String)
    record_from = Column(String)
    staff = relationship('Staff', back_populates='records')


class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialization = Column(String)
    avatar = Column(Text)
    avatar_png = Column(LargeBinary)
    rating = Column(Integer)
    votes_count = Column(Integer)
    records = relationship('Records', back_populates='staff')


class Services(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    cost = Column(Integer)
    manual_cost = Column(Integer)
    cost_per_unit = Column(Integer)
    discount = Column(Integer)
    first_cost = Column(Integer)
    amount = Column(Integer)


class Clients(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    display_name = Column(String)
    phone = Column(String)
    card = Column(String)
    email = Column(String)
    success_visits_count = Column(Integer)
    fail_visits_count = Column(Integer)
    discount = Column(Integer)
    is_new = Column(String)
    custom_fields = Column(String)



