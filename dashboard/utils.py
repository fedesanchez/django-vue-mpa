from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.db.models.query import QuerySet
from django.core.paginator import Page, Paginator
from django.forms.models import model_to_dict as base_model_to_dict

def model_to_dict(model):
  return base_model_to_dict(model, exclude=('password',))

class CustomJsonEncoder(DjangoJSONEncoder):
  def default(self, value):    
    if isinstance(value, models.Model):
      return model_to_dict(value)
    
    if isinstance(value, QuerySet):
      return [model_to_dict(model) for model in value]
    
    if isinstance(value, Page):
      return dict(
          object_list=[model_to_dict(model) for model in value],
          number=value.number,
          has_previous=value.has_previous(),
          previous_page_number=value.previous_page_number() if value.has_previous() else None,
          has_next=value.has_next(),          
          next_page_number=value.next_page_number() if value.has_next() else None,
          start_index=value.start_index(),
          end_index=value.end_index(),
          paginator=dict(num_pages=value.paginator.num_pages, count=value.paginator.count, per_page=value.paginator.per_page)
      )
      
    
    
    return super().default(value)