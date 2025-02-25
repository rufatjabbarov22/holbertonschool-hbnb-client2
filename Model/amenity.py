#!/usr/bin/python3
"""
Module that contains Amenity Model
"""
from .entity import EntityMixin, db
import json


class Amenity(db.Model, EntityMixin):
    __tablename__ = 'amenities'

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description

    def __repr__(self):
        return (f"Amenity(name={self.name}, description='{self.description}')")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'id': self.id,
            'name': self.name,
            'description': self.description
        })
        return data
