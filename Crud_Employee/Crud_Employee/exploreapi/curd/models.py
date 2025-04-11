from django.db import models

class PersonProfile(models.Model):
    """
    Represents a person's profile with contact and professional information.
    """
    DOMAIN_CHOICES = [
        ('MAC', 'MAC Domain'),
        ('DESIGN', 'Design Domain'),
        ('WEBDEV', 'Web Development Domain'),
        ('MANAGEMENT', 'Management Domain'),
        ('SOCIALS', 'Socials Domain'),
        ('OTHER', 'Other'), 
    ]

    name = models.CharField(max_length=255, help_text="Full name of the person.")
    domain = models.CharField(
        max_length=255,
        blank=True,
        choices=DOMAIN_CHOICES,  # Add choices here
        help_text="Club domain (e.g., 'MAC', 'Design'). Choose from the list."
    )
    role = models.CharField(max_length=255, blank=True, help_text="Current role (e.g., 'Web Developer', 'Cloud Engineer').")
    linkedin = models.URLField(max_length=255, blank=True, help_text="LinkedIn profile URL.")
    instagram = models.URLField(max_length=255, blank=True, help_text="Instagram profile URL.")
    email = models.EmailField(blank=True, help_text="Email address.")
    github = models.URLField(max_length=255, blank=True, help_text="GitHub profile URL.")

    def __str__(self):
        return self.name 
    class Meta:
        verbose_name = "Person Profile"
        verbose_name_plural = "Person Profiles"
        ordering = ['name'] 