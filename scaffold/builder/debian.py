
class deb:
    version = 0.1
    name = 'test-package'
    author = 'Example User'
    email = 'support@example.com'
    source = "https://code.launchpad.net/%s" % name
    
    def __init__(self, path):
        self.path = path

    def copyright(self):
        with open(self.path + 'rules', 'w') as fp:
            fp.write(
                "Format: http://dep.debian.net/deps/dep5\n"
                "Upstream-Name: %s\n" 
                "Source: <url:https://code.launchpad.net/maidstone-hackspace>\n\n"
                "Files: *\n"
                "Copyright: 2015 Maidstone Hackspace %s\n\n"
                "License:" % (self.name, self.email))

    def changelog(self):
        with open(self.path + 'changelog', 'w') as fp:
            fp.write(
                "%s (%s) trusty; urgency=low\n\n"
                "\t* Initial packaging of maidstone hackspace website.\n\n"
                "-- Oliver Marks (packaging key) <oly@digitaloctave.com>  Mon, 01 Dec 2014 11:00:00 +0100\n\n"
            )

    def control(self):
        with open(self.path + 'control', 'w') as fp:
            fp.write(
                "Source: %s\n"
                "Section: python\n"
                "Priority: optional\n"
                "Maintainer: %s <%s>\n"
                "Build-Depends: debhelper (>= 7), python-dev, python-support (>=0.3)\n"
                "Vcs-Bzr: https://launchpad.net/maidstone-hackspace\n"
                "Standards-Version: 3.9.3\n"
                "XS-Python-Version: all\n\n"
                "Package: %s\n"
                "Architecture: all\n"
                "Depends: ${python:Depends}\n"
                "Description: Maidstone Hackspace Website\n"
                " Packaged website for easy deploy to servers" % (self.name, self.author, self.email, self.name))

    def rules(self):
        with open(self.path + 'rules', 'w') as fp:
            fp.write(
                "#!/usr/bin/make -f\n"
                "# -*- makefile -*-\n\n"
                "export DH_VERBOSE=1\n\n"
                "%:\n"
                "\tdh $@\n")

    def compat(self):
        with open(self.path + 'compat', 'w') as fp:
            fp.write('9')

    def install(self):
        with open(self.path + 'install', 'w') as fp:
            fp.write('site var/www/%s' % self.name)

def render(debian_path):
    create_deb = deb(debian_path)
    create_deb.copyright()
    create_deb.changelog()
    create_deb.control()
    create_deb.rules()
    create_deb.compat()
    create_deb.install()
