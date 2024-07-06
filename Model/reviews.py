#!/usr/bin/python3
"""
Module that contains Reviews Model
"""
from .entity import Entity
import json
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Reviews(Entity):
    __tablename__ = 'reviews'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    place_id = db.Column(UUID(as_uuid=True), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return (f"Reviews(id={self.id}, place_id='{self.place_id}'"
                f"user_id='{self.user_id}', "
                f"rating='{self.rating}', comment={self.comment})")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'id': self.id,
            'place_id': str(self.place_id),
            'user_id': str(self.user_id),
            'rating': self.rating,
            'comment': self.comment,
        })
        return data
