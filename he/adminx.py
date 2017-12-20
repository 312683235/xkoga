from he.models import *
import xadmin


class CategroyAdmin(object):
    pass


class UserInfoAdmin(object):
    pass


class CodeAdmin(object):
    pass


class CommentAdmin(object):
    pass


class ContentAdmin(object):
    pass


class MechanismAdmin(object):
    pass


class linkAdmin(object):
    pass


class CityAdmin(object):
    pass


class PublicAdmin(object):
    pass


class ServerAdmin(object):
    pass


class ConsultationAdmin(object):
    pass


class CategoryAdmin(object):
    pass

xadmin.site.register(NaviCategroy,CategroyAdmin)
xadmin.site.register(UserInfo,UserInfoAdmin)
xadmin.site.register(Code,CodeAdmin)
xadmin.site.register(Comment,CommentAdmin)
xadmin.site.register(Content,ContentAdmin)
xadmin.site.register(Mechanism,MechanismAdmin)
xadmin.site.register(link,linkAdmin)
xadmin.site.register(City,CityAdmin)
xadmin.site.register(Public,PublicAdmin)
xadmin.site.register(Server,ServerAdmin)
xadmin.site.register(Consultation,ConsultationAdmin)
xadmin.site.register(Category,CategoryAdmin)
