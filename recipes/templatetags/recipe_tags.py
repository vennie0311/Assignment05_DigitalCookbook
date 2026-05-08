from django import template

register = template.Library()


@register.filter
def format_minutes(value):
    try:
        total_minutes = int(value)
    except (TypeError, ValueError):
        return '0 mins'

    hours = total_minutes // 60
    minutes = total_minutes % 60
    parts = []
    if hours:
        parts.append(f"{hours} hr" + ("s" if hours != 1 else ""))
    if minutes:
        parts.append(f"{minutes} mins")
    return ' '.join(parts) if parts else '0 mins'
