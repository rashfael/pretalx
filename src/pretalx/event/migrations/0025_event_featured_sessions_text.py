# Generated by Django 3.1.4 on 2020-12-13 23:27

from django.db import migrations
import i18nfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0024_remove_team_review_override_votes"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="featured_sessions_text",
            field=i18nfield.fields.I18nTextField(null=True),
        ),
    ]
