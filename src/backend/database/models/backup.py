from sqlalchemy import Column, JSON, ForeignKey, UUID
from sqlalchemy.orm import relationship

from .base import TimestampedBase

class Backup(TimestampedBase):
    """Model for backups table in padws schema"""
    __tablename__ = "backups"
    __table_args__ = {"schema": "padws"}
    
    pad_id = Column(UUID(as_uuid=True), ForeignKey("padws.pads.id"), nullable=False)
    data = Column(JSON, nullable=False)
    
    pad = relationship("Pad", back_populates="backups")
    
    def __repr__(self):
        return f"<Backup(id={self.id}, pad_id='{self.pad_id}')>"
