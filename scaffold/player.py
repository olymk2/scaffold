from web import web

web.page.header('header')

web.buttons.add('','img/player_rew.png','Previous')
web.buttons.add('','img/player_play.png','Previous')
web.buttons.add('','img/player_fwd.png','Previous')

web.container.append(web.buttons.render())
web.page.section(web.container.render())

web.boxes.add('0')
web.boxes.add('25')
web.boxes.add('50')
web.boxes.add('75')
web.boxes.add('100')
web.container.append(web.boxes.render())

web.page.section(web.container.render())
print(web.page.render())
