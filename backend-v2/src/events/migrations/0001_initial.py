# Generated by Django 2.2.1 on 2019-06-04 12:49

from django.db import migrations, models
import django.db.models.deletion
import src.events.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('action', models.CharField(choices=[(src.events.models.EventAction('Created'), 'Created'), (src.events.models.EventAction('Generic Update'), 'Generic Update'), (src.events.models.EventAction('Attribute change requested'), 'Attribute change requested'), (src.events.models.EventAction('Attribute change approved'), 'Attribute change approved'), (src.events.models.EventAction('Attribute changed'), 'Attribute changed'), (src.events.models.EventAction('Attribute change rejected'), 'Attribute change rejected'), (src.events.models.EventAction('Commented'), 'Commented'), (src.events.models.EventAction('Outcome added'), 'Outcome added'), (src.events.models.EventAction('Entity assigned'), 'Entity assigned'), (src.events.models.EventAction('Entity removed'), 'Entity removed')], max_length=50)),
                ('reference_id', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('intiator', models.IntegerField()),
                ('affected_attribute', models.CharField(choices=[(src.events.models.AffectedAttribute('Status'), 'Status'), (src.events.models.AffectedAttribute('Severity'), 'Severity'), (src.events.models.AffectedAttribute('Outcome'), 'Outcome')], max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('incident_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='incidents.Incident')),
                ('linked_event_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.Event')),
            ],
            options={
                'ordering': ('created_date',),
            },
        ),
    ]