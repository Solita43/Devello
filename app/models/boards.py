from .db import db, environment, SCHEMA, add_prefix_for_prod

class Board(db.Model):
    __tablename__ = "boards"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('projects.id')), nullable=False)
    purpose = db.Column(db.String(50), nullable=False)

    project = db.relationship("Project", back_populates="boards")
    cards = db.relationship("Card", back_populates="board", cascade="delete-orphan, all")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "projectId": self.project_id,
            "purpose": self.purpose,
            "cards": {card.order: card.to_dict() for card in self.cards}
        }