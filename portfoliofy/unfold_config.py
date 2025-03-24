from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def generate_unfold_config(brand_name: str, frontend_url: str):
    return {
        "SITE_TITLE": _(f"{brand_name} ADMIN"),
        "SITE_HEADER": _(f"{brand_name} ADMINISTRATION"),
        "SITE_URL": frontend_url,
        "SITE_ICON": f"{frontend_url}/logo.svg",

        "SITE_LOGO":  f"{frontend_url}/logo.svg",

        "SITE_SYMBOL": "grass",
        "SITE_FAVICONS": [
            {
                "rel": "icon",
                "sizes": "32x32",
                "type": "image/svg+xml",
                "href": f"{frontend_url}/logo.svg",
            },
        ],
        "SHOW_HISTORY": True,
        "SHOW_VIEW_ON_SITE": True,
        # "DASHBOARD_CALLBACK": "dashboard.views.dashboard_callback",
        "STYLES": [
            lambda request: static("css/styles.css"),
        ],
        "COLORS": {
            "base": {
                "50": "250 250 250",
                "100": "245 245 245",
                "200": "229 229 229",
                "300": "212 212 212",
                "400": "163 163 163",
                "500": "115 115 115",
                "600": "82 82 82",
                "700": "64 64 64",
                "800": "38 38 38",
                "900": "23 23 23",
                "950": "10 10 10",
            },
            "font": {
                "subtle-light": "107 114 128",
                "subtle-dark": "156 163 175",
                "default-light": "75 85 99",
                "default-dark": "209 213 219",
                "important-light": "17 24 39",
                "important-dark": "243 244 246",
            },
            "primary": {
                "50": "250 245 255",
                "100": "243 232 255",
                "200": "233 213 255",
                "300": "216 180 254",
                "400": "192 132 252",
                "500": "168 85 247",
                "600": "147 51 234",
                "700": "126 34 206",
                "800": "107 33 168",
                "900": "88 28 135",
                "950": "59 7 100",
            },
        },
        "SIDEBAR": {
            "show_search": True,
            "show_all_applications": False,
            "navigation": [
                # Supported icon set: https://fonts.google.com/icons
                {
                    "title": _("Portfoliofy"),
                    "separator": True,
                    "items": [
                        {
                            "title": _("Dashboard"),
                            "icon": "speed",
                            "link": reverse_lazy("admin:index"),
                            "permission": lambda request: request.user.is_superuser,
                        },
                        {
                            "title": _("Projects"),
                            "icon": "workspace_premium",
                            "link": reverse_lazy("admin:core_project_changelist"),
                        },
                        {
                            "title": _("Testimonials"),
                            "icon": "star",
                            "link": reverse_lazy("admin:core_testimonial_changelist"),
                        },
                    ],
                },

                {
                    "title": _("Blog"),
                    "items": [
                        {
                            "title": _("Categories"),
                            "icon": "category",
                            "link": reverse_lazy("admin:blog_category_changelist"),
                        },
                        {
                            "title": _("Posts"),
                            "icon": "article",
                            "link": reverse_lazy("admin:blog_post_changelist"),
                        },
                    ],
                },

                {
                    "title": _("Users and Groups"),
                    "collapsible": True,
                    "items": [
                        {
                            "title": _("Users"),
                            "icon": "person",
                            "link": reverse_lazy("admin:auth_user_changelist"),
                        },
                        {
                            "title": _("Groups"),
                            "icon": "group",
                            "link": reverse_lazy("admin:auth_group_changelist"),
                        },
                    ],
                },

            ],
        },
    }
