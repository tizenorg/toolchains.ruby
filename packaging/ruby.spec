%define rubyver         1.9.2
%define rubyminorver    p290

Name: ruby
Summary: An interpreter of object-oriented scripting language
Version: %{rubyver}
Release: 1
Group: Development/Languages
License: Ruby License/GPL
URL: http://www.ruby-lang.org
Source0: %{name}-%{version}.tar.gz

#!BuildIgnore: ruby-x86-arm

%description
Ruby is the interpreted scripting language for quick and easy object-oriented programming.
It has many features to process text files and to do system management tasks (as in Perl).
It is simple, straight-forward, and extensible.

%prep
%setup

%build
%configure \
  --disable-install-doc \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir}

%ifarch %{arm}
%ifarch armv7el armv7l
%define platform    armv7l-linux-eabi
%else
%define platform    armv7hl-linux-eabi
%endif
%else
%define platform    i586-linux
%endif

make

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)

%{_bindir}/*

%{_includedir}/ruby/ruby-1.9.1/*
%{_includedir}/ruby/ruby-1.9.1/ruby/*
%{_includedir}/ruby/ruby-1.9.1/ruby/backward/*
%{_includedir}/ruby/ruby-1.9.1/%{platform}/ruby/*

%{_libdir}/libruby-static.a
%{_libdir}/ruby/gems/1.9.1/specifications/*
%{_libdir}/ruby/1.9.1/*
%{_libdir}/ruby/1.9.1/bigdecimal/*
%{_libdir}/ruby/1.9.1/cgi/*
%{_libdir}/ruby/1.9.1/cgi/session/*
%{_libdir}/ruby/1.9.1/date/*
%{_libdir}/ruby/1.9.1/date/delta/*
%{_libdir}/ruby/1.9.1/digest/*
%{_libdir}/ruby/1.9.1/dl/*
%{_libdir}/ruby/1.9.1/drb/*
%{_libdir}/ruby/1.9.1/%{platform}/*
%{_libdir}/ruby/1.9.1/%{platform}/digest/*
%{_libdir}/ruby/1.9.1/%{platform}/dl/*
%{_libdir}/ruby/1.9.1/%{platform}/enc/*
%{_libdir}/ruby/1.9.1/%{platform}/enc/trans/*
%{_libdir}/ruby/1.9.1/%{platform}/io/*
%{_libdir}/ruby/1.9.1/%{platform}/json/ext/*
%{_libdir}/ruby/1.9.1/%{platform}/mathn/*
%{_libdir}/ruby/1.9.1/%{platform}/racc/*
%{_libdir}/ruby/1.9.1/irb/*
%{_libdir}/ruby/1.9.1/irb/cmd/*
%{_libdir}/ruby/1.9.1/irb/ext/*
%{_libdir}/ruby/1.9.1/irb/lc/*
%{_libdir}/ruby/1.9.1/irb/lc/ja/*
%{_libdir}/ruby/1.9.1/json/*
%{_libdir}/ruby/1.9.1/json/add/*
%{_libdir}/ruby/1.9.1/minitest/*
%{_libdir}/ruby/1.9.1/net/*
%{_libdir}/ruby/1.9.1/optparse/*
%{_libdir}/ruby/1.9.1/racc/*
%{_libdir}/ruby/1.9.1/rake/*
%{_libdir}/ruby/1.9.1/rake/contrib/*
%{_libdir}/ruby/1.9.1/rake/loaders/*
%{_libdir}/ruby/1.9.1/rbconfig/*
%{_libdir}/ruby/1.9.1/rdoc/*
%{_libdir}/ruby/1.9.1/rdoc/generator/*
%{_libdir}/ruby/1.9.1/rdoc/generator/template/darkfish/*
%{_libdir}/ruby/1.9.1/rdoc/generator/template/darkfish/images/*
%{_libdir}/ruby/1.9.1/rdoc/generator/template/darkfish/js/*
%{_libdir}/ruby/1.9.1/rdoc/markup/*
%{_libdir}/ruby/1.9.1/rdoc/parser/*
%{_libdir}/ruby/1.9.1/rdoc/ri/*
%{_libdir}/ruby/1.9.1/rexml/*
%{_libdir}/ruby/1.9.1/rexml/dtd/*
%{_libdir}/ruby/1.9.1/rexml/encodings/*
%{_libdir}/ruby/1.9.1/rexml/formatters/*
%{_libdir}/ruby/1.9.1/rexml/light/*
%{_libdir}/ruby/1.9.1/rexml/parsers/*
%{_libdir}/ruby/1.9.1/rexml/validation/*
%{_libdir}/ruby/1.9.1/rinda/*
%{_libdir}/ruby/1.9.1/rss/*
%{_libdir}/ruby/1.9.1/rss/content/*
%{_libdir}/ruby/1.9.1/rss/dublincore/*
%{_libdir}/ruby/1.9.1/rss/maker/*
%{_libdir}/ruby/1.9.1/rubygems/*
%{_libdir}/ruby/1.9.1/rubygems/commands/*
%{_libdir}/ruby/1.9.1/rubygems/ext/*
%{_libdir}/ruby/1.9.1/rubygems/package/*
%{_libdir}/ruby/1.9.1/rubygems/package/tar_reader/*
%{_libdir}/ruby/1.9.1/shell/*
%{_libdir}/ruby/1.9.1/syck/*
%{_libdir}/ruby/1.9.1/test/*
%{_libdir}/ruby/1.9.1/test/unit/*
%{_libdir}/ruby/1.9.1/uri/*
%{_libdir}/ruby/1.9.1/webrick/*
%{_libdir}/ruby/1.9.1/webrick/httpauth/*
%{_libdir}/ruby/1.9.1/webrick/httpservlet/*
%{_libdir}/ruby/1.9.1/xmlrpc/*
%{_libdir}/ruby/1.9.1/yaml/*

%{_mandir}/man1/*
