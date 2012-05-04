from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache

from flatblocks.settings import CACHE_PREFIX


class FlatBlock(models.Model):
    """
    Think of a flatblock as a flatpage but for just part of a site. It's
    basically a piece of content with a given name (slug) and an optional
    title (header) which you can, for example, use in a sidebar of a website.
    """
    namespace = models.CharField(max_length=255, unique=True,
        verbose_name=_('Namespace'),
        help_text=_("A unique name used for reference in the templates"))
    description = models.CharField(blank=True, null=True, max_length=255,
        verbose_name=_('Description'),
        help_text=_("A description for the content this block represents"))
    content = models.TextField(verbose_name=_('Content'), blank=True,
                null=True)

    def __unicode__(self):
        return u"%s" % (self.namespace,)

    def save(self, *args, **kwargs):
        super(FlatBlock, self).save(*args, **kwargs)
        # Now also invalidate the cache used in the templatetag
        cache.delete('%s%s' % (CACHE_PREFIX, self.namespace, ))

    class Meta:
        verbose_name = _('Flat block')
        verbose_name_plural = _('Flat blocks')
