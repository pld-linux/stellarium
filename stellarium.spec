#
# TODO:
#  - automate packaging all fancy translations
#
%define guide_version	1
%define	qt_ver		5.9.0
Summary:	Realistic sky generator
Summary(pl.UTF-8):	Realistyczny generator obrazu nieba
Name:		stellarium
Version:	0.22.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Science
Source0:	https://github.com/Stellarium/stellarium/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2aafc25f5736b8b5d6d2bcf6d7c2d118
Source1:	https://github.com/Stellarium/stellarium/releases/download/v%{version}/%{name}_user_guide-%{version}-%{guide_version}.pdf
# Source1-md5:	f7dde2777d41d2b5626de4fbce44db6c
URL:		http://stellarium.org/
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Charts-devel >= %{qt_ver}
BuildRequires:	Qt5Concurrent-devel >= %{qt_ver}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Multimedia-devel >= %{qt_ver}
BuildRequires:	Qt5MultimediaWidgets-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5OpenGL-devel >= %{qt_ver}
BuildRequires:	Qt5Positioning-devel >= %{qt_ver}
BuildRequires:	Qt5Script-devel >= %{qt_ver}
BuildRequires:	Qt5SerialPort-devel >= %{qt_ver}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.10.0
BuildRequires:	doxygen
BuildRequires:	gettext-tools
# API version >= 6.0
BuildRequires:	gpsd-devel >= 3
BuildRequires:	libstdc++-devel >= 6:7
# pod2man
BuildRequires:	perl-tools-pod
BuildRequires:	python3 >= 1:3
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-linguist >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
Requires:	Qt5Gui-platform-xcb-glx >= %{qt_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stellarium renders 3D realistic skies in real time with OpenGL. It
displays stars, constellations, planets, nebulas and others things
like ground, landscape, fog, etc. Main features:
- Over 120000 stars from the Hipparcos Catalogue with name and infos
  for the brightest ones.
- Planets in real time, with a powerfull zoom mode.
- Drawing of the 88 constellations with their names.
- More than 40 messiers objects (Orion, M31 etc..).
- Photorealistic Milky Way.
- Ground, fog, and landscape.
- Star twinkling.
- Time control (real time and accelered time modes).
- Clikable stars, planets and nebulas with informations.
- Smooth real time navigation.
- Windowed and fullscreen modes.

%description -l pl.UTF-8
Stellarium przy pomocy OpenGL-a oddaje w czasie rzeczywistym
trójwymiarowe, realistyczne obrazy nieba. Wyświetla gwiazdy,
konstelacje, planety, mgławice i inne obiekty takie jak powierzchnia
ziemi, krajobrazy, mgła, itp. Główne cechy to:
- Ponad 120000 gwiazd z "Hipparcos Catalogue" z nazwami i opisem
  najjaśniejszych.
- Planety w czasie rzeczywistym z możliwością dużego powiększania.
- Wyświetlanie 88 konstelacji wraz z ich nazwami.
- Ponad 40 obiektów messiera (Orion, M31, itp...).
- Realistyczna Droga Mleczna.
- Powierzchnia, mgła i krajobraz.
- Migotanie gwiazd.
- Kontrola czasu (tryby czasu rzeczywistego i przyśpieszonego).
- Dostęp do informacji na temat gwiazd, planet i mgławic po ich
  kliknięciu.
- Płynna nawigacja w czasie rzeczywistym.
- Tryb pracy pełnoekranowej i w oknie.

%package data
Summary:	Stellarium data files
Summary(pl.UTF-8):	Pliki danych dla Stellarium
Group:		X11/Applications/Science
BuildArch:	noarch

%description data
Stellarium data files.

%description data -l pl.UTF-8
Pliki danych dla Stellarium.

%prep
%setup -q

cp -p %{SOURCE1} .

%build
install -d build
cd build
%cmake .. \
	-DBUILD_SHARED_LIBS=OFF

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/translations/stellarium*/es_419.qm
# sync scripts with libc
for domain in stellarium stellarium-planetary-features stellarium-remotecontrol stellarium-scripts stellarium-skycultures ; do
	%{__mv} $RPM_BUILD_ROOT%{_datadir}/%{name}/translations/${domain}/{uz,uz@cyrillic}.qm
	%{__mv} $RPM_BUILD_ROOT%{_datadir}/%{name}/translations/${domain}/{uz@Latn,uz}.qm
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS.md ChangeLog README.md %{name}_user_guide-%{version}-%{guide_version}.pdf
%attr(755,root,root) %{_bindir}/stellarium
%{_datadir}/metainfo/org.stellarium.Stellarium.appdata.xml
%{_datadir}/mime/packages/stellarium.xml
%{_desktopdir}/org.stellarium.Stellarium.desktop
%{_iconsdir}/hicolor/*x*/apps/stellarium.png
%{_mandir}/man1/stellarium.1*

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
%{_datadir}/%{name}/landscapes
%{_datadir}/%{name}/models
%{_datadir}/%{name}/nebulae
%{_datadir}/%{name}/scenery3d
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/skycultures
%{_datadir}/%{name}/stars
%{_datadir}/%{name}/textures
%{_datadir}/%{name}/webroot
%dir %{_datadir}/%{name}/translations
%dir %{_datadir}/%{name}/translations/stellarium
%lang(aa) %{_datadir}/%{name}/translations/stellarium/aa.qm
%lang(ae) %{_datadir}/%{name}/translations/stellarium/ae.qm
%lang(af) %{_datadir}/%{name}/translations/stellarium/af.qm
%lang(ak) %{_datadir}/%{name}/translations/stellarium/ak.qm
%lang(am) %{_datadir}/%{name}/translations/stellarium/am.qm
%lang(ar) %{_datadir}/%{name}/translations/stellarium/ar.qm
%lang(ast) %{_datadir}/%{name}/translations/stellarium/ast.qm
%lang(av) %{_datadir}/%{name}/translations/stellarium/av.qm
%lang(az) %{_datadir}/%{name}/translations/stellarium/az.qm
%lang(be) %{_datadir}/%{name}/translations/stellarium/be.qm
%lang(ber) %{_datadir}/%{name}/translations/stellarium/ber.qm
%lang(bg) %{_datadir}/%{name}/translations/stellarium/bg.qm
%lang(bh) %{_datadir}/%{name}/translations/stellarium/bh.qm
%lang(bi) %{_datadir}/%{name}/translations/stellarium/bi.qm
%lang(bn) %{_datadir}/%{name}/translations/stellarium/bn.qm
%lang(br) %{_datadir}/%{name}/translations/stellarium/br.qm
%lang(bs) %{_datadir}/%{name}/translations/stellarium/bs.qm
%lang(ca) %{_datadir}/%{name}/translations/stellarium/ca.qm
%lang(ca@valencia) %{_datadir}/%{name}/translations/stellarium/ca@valencia.qm
%lang(ce) %{_datadir}/%{name}/translations/stellarium/ce.qm
%lang(cnr) %{_datadir}/%{name}/translations/stellarium/cnr.qm
%lang(cs) %{_datadir}/%{name}/translations/stellarium/cs.qm
%lang(cv) %{_datadir}/%{name}/translations/stellarium/cv.qm
%lang(da) %{_datadir}/%{name}/translations/stellarium/da.qm
%lang(de) %{_datadir}/%{name}/translations/stellarium/de.qm
%lang(el) %{_datadir}/%{name}/translations/stellarium/el.qm
%lang(en) %{_datadir}/%{name}/translations/stellarium/en.qm
%lang(en_AU) %{_datadir}/%{name}/translations/stellarium/en_AU.qm
%lang(en_CA) %{_datadir}/%{name}/translations/stellarium/en_CA.qm
%lang(en_GB) %{_datadir}/%{name}/translations/stellarium/en_GB.qm
%lang(en_IN) %{_datadir}/%{name}/translations/stellarium/en_IN.qm
%lang(en_US) %{_datadir}/%{name}/translations/stellarium/en_US.qm
%lang(eo) %{_datadir}/%{name}/translations/stellarium/eo.qm
%lang(es) %{_datadir}/%{name}/translations/stellarium/es.qm
%lang(es_AR) %{_datadir}/%{name}/translations/stellarium/es_AR.qm
%lang(es_CL) %{_datadir}/%{name}/translations/stellarium/es_CL.qm
%lang(et) %{_datadir}/%{name}/translations/stellarium/et.qm
%lang(eu) %{_datadir}/%{name}/translations/stellarium/eu.qm
%lang(fa) %{_datadir}/%{name}/translations/stellarium/fa.qm
%lang(fi) %{_datadir}/%{name}/translations/stellarium/fi.qm
%lang(fj) %{_datadir}/%{name}/translations/stellarium/fj.qm
%lang(fr) %{_datadir}/%{name}/translations/stellarium/fr.qm
%lang(fr_CA) %{_datadir}/%{name}/translations/stellarium/fr_CA.qm
%lang(fy) %{_datadir}/%{name}/translations/stellarium/fy.qm
%lang(ga) %{_datadir}/%{name}/translations/stellarium/ga.qm
%lang(gd) %{_datadir}/%{name}/translations/stellarium/gd.qm
%lang(gl) %{_datadir}/%{name}/translations/stellarium/gl.qm
%lang(gn) %{_datadir}/%{name}/translations/stellarium/gn.qm
%lang(gu) %{_datadir}/%{name}/translations/stellarium/gu.qm
%lang(gv) %{_datadir}/%{name}/translations/stellarium/gv.qm
%lang(he) %{_datadir}/%{name}/translations/stellarium/he.qm
%lang(hi) %{_datadir}/%{name}/translations/stellarium/hi.qm
%lang(hr) %{_datadir}/%{name}/translations/stellarium/hr.qm
%lang(hrx) %{_datadir}/%{name}/translations/stellarium/hrx.qm
%lang(hu) %{_datadir}/%{name}/translations/stellarium/hu.qm
%lang(hy) %{_datadir}/%{name}/translations/stellarium/hy.qm
%lang(id) %{_datadir}/%{name}/translations/stellarium/id.qm
%lang(is) %{_datadir}/%{name}/translations/stellarium/is.qm
%lang(it) %{_datadir}/%{name}/translations/stellarium/it.qm
%lang(ja) %{_datadir}/%{name}/translations/stellarium/ja.qm
%lang(jv) %{_datadir}/%{name}/translations/stellarium/jv.qm
%lang(ka) %{_datadir}/%{name}/translations/stellarium/ka.qm
%lang(kg) %{_datadir}/%{name}/translations/stellarium/kg.qm
%lang(kk) %{_datadir}/%{name}/translations/stellarium/kk.qm
%lang(kn) %{_datadir}/%{name}/translations/stellarium/kn.qm
%lang(ko) %{_datadir}/%{name}/translations/stellarium/ko.qm
%lang(krl) %{_datadir}/%{name}/translations/stellarium/krl.qm
%lang(ku) %{_datadir}/%{name}/translations/stellarium/ku.qm
%lang(ky) %{_datadir}/%{name}/translations/stellarium/ky.qm
%lang(la) %{_datadir}/%{name}/translations/stellarium/la.qm
%lang(lb) %{_datadir}/%{name}/translations/stellarium/lb.qm
%lang(lt) %{_datadir}/%{name}/translations/stellarium/lt.qm
%lang(lv) %{_datadir}/%{name}/translations/stellarium/lv.qm
%lang(mk) %{_datadir}/%{name}/translations/stellarium/mk.qm
%lang(ml) %{_datadir}/%{name}/translations/stellarium/ml.qm
%lang(mn) %{_datadir}/%{name}/translations/stellarium/mn.qm
%lang(mo) %{_datadir}/%{name}/translations/stellarium/mo.qm
%lang(mr) %{_datadir}/%{name}/translations/stellarium/mr.qm
%lang(ms) %{_datadir}/%{name}/translations/stellarium/ms.qm
%lang(my) %{_datadir}/%{name}/translations/stellarium/my.qm
%lang(na) %{_datadir}/%{name}/translations/stellarium/na.qm
%lang(nb) %{_datadir}/%{name}/translations/stellarium/nb.qm
%lang(nds) %{_datadir}/%{name}/translations/stellarium/nds.qm
%lang(ne) %{_datadir}/%{name}/translations/stellarium/ne.qm
%lang(nl) %{_datadir}/%{name}/translations/stellarium/nl.qm
%lang(nn) %{_datadir}/%{name}/translations/stellarium/nn.qm
%lang(oj) %{_datadir}/%{name}/translations/stellarium/oj.qm
%lang(pa) %{_datadir}/%{name}/translations/stellarium/pa.qm
%lang(pl) %{_datadir}/%{name}/translations/stellarium/pl.qm
%lang(pt) %{_datadir}/%{name}/translations/stellarium/pt.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/stellarium/pt_BR.qm
%lang(ro) %{_datadir}/%{name}/translations/stellarium/ro.qm
%lang(ru) %{_datadir}/%{name}/translations/stellarium/ru.qm
%lang(sc) %{_datadir}/%{name}/translations/stellarium/sc.qm
%lang(si) %{_datadir}/%{name}/translations/stellarium/si.qm
%lang(sk) %{_datadir}/%{name}/translations/stellarium/sk.qm
%lang(sl) %{_datadir}/%{name}/translations/stellarium/sl.qm
%lang(sq) %{_datadir}/%{name}/translations/stellarium/sq.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium/sr.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium/sr@latin.qm
%lang(sv) %{_datadir}/%{name}/translations/stellarium/sv.qm
%lang(sw) %{_datadir}/%{name}/translations/stellarium/sw.qm
%lang(ta) %{_datadir}/%{name}/translations/stellarium/ta.qm
%lang(te) %{_datadir}/%{name}/translations/stellarium/te.qm
%lang(tg) %{_datadir}/%{name}/translations/stellarium/tg.qm
%lang(th) %{_datadir}/%{name}/translations/stellarium/th.qm
%lang(tl) %{_datadir}/%{name}/translations/stellarium/tl.qm
%lang(tr) %{_datadir}/%{name}/translations/stellarium/tr.qm
%lang(tzm) %{_datadir}/%{name}/translations/stellarium/tzm.qm
%lang(ug) %{_datadir}/%{name}/translations/stellarium/ug.qm
%lang(uk) %{_datadir}/%{name}/translations/stellarium/uk.qm
%lang(ur) %{_datadir}/%{name}/translations/stellarium/ur.qm
%lang(uz) %{_datadir}/%{name}/translations/stellarium/uz.qm
%lang(uz) %{_datadir}/%{name}/translations/stellarium/uz@cyrillic.qm
%lang(vi) %{_datadir}/%{name}/translations/stellarium/vi.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/stellarium/zh_CN.qm
%lang(zh_HK) %{_datadir}/%{name}/translations/stellarium/zh_HK.qm
%lang(zh_SG) %{_datadir}/%{name}/translations/stellarium/zh_SG.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/stellarium/zh_TW.qm
%dir %{_datadir}/%{name}/translations/stellarium-planetary-features
%lang(af) %{_datadir}/%{name}/translations/stellarium-planetary-features/af.qm
%lang(ak) %{_datadir}/%{name}/translations/stellarium-planetary-features/ak.qm
%lang(am) %{_datadir}/%{name}/translations/stellarium-planetary-features/am.qm
%lang(ar) %{_datadir}/%{name}/translations/stellarium-planetary-features/ar.qm
%lang(ast) %{_datadir}/%{name}/translations/stellarium-planetary-features/ast.qm
%lang(az) %{_datadir}/%{name}/translations/stellarium-planetary-features/az.qm
%lang(be) %{_datadir}/%{name}/translations/stellarium-planetary-features/be.qm
%lang(bg) %{_datadir}/%{name}/translations/stellarium-planetary-features/bg.qm
%lang(bn) %{_datadir}/%{name}/translations/stellarium-planetary-features/bn.qm
%lang(br) %{_datadir}/%{name}/translations/stellarium-planetary-features/br.qm
%lang(bs) %{_datadir}/%{name}/translations/stellarium-planetary-features/bs.qm
%lang(ca) %{_datadir}/%{name}/translations/stellarium-planetary-features/ca.qm
%lang(ca@valencia) %{_datadir}/%{name}/translations/stellarium-planetary-features/ca@valencia.qm
%lang(cnr) %{_datadir}/%{name}/translations/stellarium-planetary-features/cnr.qm
%lang(cs) %{_datadir}/%{name}/translations/stellarium-planetary-features/cs.qm
%lang(cv) %{_datadir}/%{name}/translations/stellarium-planetary-features/cv.qm
%lang(da) %{_datadir}/%{name}/translations/stellarium-planetary-features/da.qm
%lang(de) %{_datadir}/%{name}/translations/stellarium-planetary-features/de.qm
%lang(el) %{_datadir}/%{name}/translations/stellarium-planetary-features/el.qm
%lang(en) %{_datadir}/%{name}/translations/stellarium-planetary-features/en.qm
%lang(en_AU) %{_datadir}/%{name}/translations/stellarium-planetary-features/en_AU.qm
%lang(en_CA) %{_datadir}/%{name}/translations/stellarium-planetary-features/en_CA.qm
%lang(en_GB) %{_datadir}/%{name}/translations/stellarium-planetary-features/en_GB.qm
%lang(en_IN) %{_datadir}/%{name}/translations/stellarium-planetary-features/en_IN.qm
%lang(en_US) %{_datadir}/%{name}/translations/stellarium-planetary-features/en_US.qm
%lang(eo) %{_datadir}/%{name}/translations/stellarium-planetary-features/eo.qm
%lang(es) %{_datadir}/%{name}/translations/stellarium-planetary-features/es.qm
%lang(es_AR) %{_datadir}/%{name}/translations/stellarium-planetary-features/es_AR.qm
%lang(es_CL) %{_datadir}/%{name}/translations/stellarium-planetary-features/es_CL.qm
%lang(et) %{_datadir}/%{name}/translations/stellarium-planetary-features/et.qm
%lang(eu) %{_datadir}/%{name}/translations/stellarium-planetary-features/eu.qm
%lang(fa) %{_datadir}/%{name}/translations/stellarium-planetary-features/fa.qm
%lang(fi) %{_datadir}/%{name}/translations/stellarium-planetary-features/fi.qm
%lang(fr) %{_datadir}/%{name}/translations/stellarium-planetary-features/fr.qm
%lang(fr_CA) %{_datadir}/%{name}/translations/stellarium-planetary-features/fr_CA.qm
%lang(fy) %{_datadir}/%{name}/translations/stellarium-planetary-features/fy.qm
%lang(ga) %{_datadir}/%{name}/translations/stellarium-planetary-features/ga.qm
%lang(gd) %{_datadir}/%{name}/translations/stellarium-planetary-features/gd.qm
%lang(gl) %{_datadir}/%{name}/translations/stellarium-planetary-features/gl.qm
%lang(gu) %{_datadir}/%{name}/translations/stellarium-planetary-features/gu.qm
%lang(he) %{_datadir}/%{name}/translations/stellarium-planetary-features/he.qm
%lang(hi) %{_datadir}/%{name}/translations/stellarium-planetary-features/hi.qm
%lang(hr) %{_datadir}/%{name}/translations/stellarium-planetary-features/hr.qm
%lang(hu) %{_datadir}/%{name}/translations/stellarium-planetary-features/hu.qm
%lang(hy) %{_datadir}/%{name}/translations/stellarium-planetary-features/hy.qm
%lang(id) %{_datadir}/%{name}/translations/stellarium-planetary-features/id.qm
%lang(is) %{_datadir}/%{name}/translations/stellarium-planetary-features/is.qm
%lang(it) %{_datadir}/%{name}/translations/stellarium-planetary-features/it.qm
%lang(ja) %{_datadir}/%{name}/translations/stellarium-planetary-features/ja.qm
%lang(jv) %{_datadir}/%{name}/translations/stellarium-planetary-features/jv.qm
%lang(ka) %{_datadir}/%{name}/translations/stellarium-planetary-features/ka.qm
%lang(kk) %{_datadir}/%{name}/translations/stellarium-planetary-features/kk.qm
%lang(kn) %{_datadir}/%{name}/translations/stellarium-planetary-features/kn.qm
%lang(ko) %{_datadir}/%{name}/translations/stellarium-planetary-features/ko.qm
%lang(krl) %{_datadir}/%{name}/translations/stellarium-planetary-features/krl.qm
%lang(ku) %{_datadir}/%{name}/translations/stellarium-planetary-features/ku.qm
%lang(ky) %{_datadir}/%{name}/translations/stellarium-planetary-features/ky.qm
%lang(la) %{_datadir}/%{name}/translations/stellarium-planetary-features/la.qm
%lang(lb) %{_datadir}/%{name}/translations/stellarium-planetary-features/lb.qm
%lang(lt) %{_datadir}/%{name}/translations/stellarium-planetary-features/lt.qm
%lang(lv) %{_datadir}/%{name}/translations/stellarium-planetary-features/lv.qm
%lang(mk) %{_datadir}/%{name}/translations/stellarium-planetary-features/mk.qm
%lang(ml) %{_datadir}/%{name}/translations/stellarium-planetary-features/ml.qm
%lang(mn) %{_datadir}/%{name}/translations/stellarium-planetary-features/mn.qm
%lang(mr) %{_datadir}/%{name}/translations/stellarium-planetary-features/mr.qm
%lang(ms) %{_datadir}/%{name}/translations/stellarium-planetary-features/ms.qm
%lang(my) %{_datadir}/%{name}/translations/stellarium-planetary-features/my.qm
%lang(nb) %{_datadir}/%{name}/translations/stellarium-planetary-features/nb.qm
%lang(nds) %{_datadir}/%{name}/translations/stellarium-planetary-features/nds.qm
%lang(ne) %{_datadir}/%{name}/translations/stellarium-planetary-features/ne.qm
%lang(nl) %{_datadir}/%{name}/translations/stellarium-planetary-features/nl.qm
%lang(nn) %{_datadir}/%{name}/translations/stellarium-planetary-features/nn.qm
%lang(pa) %{_datadir}/%{name}/translations/stellarium-planetary-features/pa.qm
%lang(pl) %{_datadir}/%{name}/translations/stellarium-planetary-features/pl.qm
%lang(pt) %{_datadir}/%{name}/translations/stellarium-planetary-features/pt.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/stellarium-planetary-features/pt_BR.qm
%lang(ro) %{_datadir}/%{name}/translations/stellarium-planetary-features/ro.qm
%lang(ru) %{_datadir}/%{name}/translations/stellarium-planetary-features/ru.qm
%lang(sc) %{_datadir}/%{name}/translations/stellarium-planetary-features/sc.qm
%lang(si) %{_datadir}/%{name}/translations/stellarium-planetary-features/si.qm
%lang(sk) %{_datadir}/%{name}/translations/stellarium-planetary-features/sk.qm
%lang(sl) %{_datadir}/%{name}/translations/stellarium-planetary-features/sl.qm
%lang(sq) %{_datadir}/%{name}/translations/stellarium-planetary-features/sq.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium-planetary-features/sr.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium-planetary-features/sr@latin.qm
%lang(sv) %{_datadir}/%{name}/translations/stellarium-planetary-features/sv.qm
%lang(sw) %{_datadir}/%{name}/translations/stellarium-planetary-features/sw.qm
%lang(ta) %{_datadir}/%{name}/translations/stellarium-planetary-features/ta.qm
%lang(te) %{_datadir}/%{name}/translations/stellarium-planetary-features/te.qm
%lang(tg) %{_datadir}/%{name}/translations/stellarium-planetary-features/tg.qm
%lang(th) %{_datadir}/%{name}/translations/stellarium-planetary-features/th.qm
%lang(tl) %{_datadir}/%{name}/translations/stellarium-planetary-features/tl.qm
%lang(tr) %{_datadir}/%{name}/translations/stellarium-planetary-features/tr.qm
%lang(tzm) %{_datadir}/%{name}/translations/stellarium-planetary-features/tzm.qm
%lang(ug) %{_datadir}/%{name}/translations/stellarium-planetary-features/ug.qm
%lang(uk) %{_datadir}/%{name}/translations/stellarium-planetary-features/uk.qm
%lang(ur) %{_datadir}/%{name}/translations/stellarium-planetary-features/ur.qm
%lang(uz) %{_datadir}/%{name}/translations/stellarium-planetary-features/uz.qm
%lang(uz) %{_datadir}/%{name}/translations/stellarium-planetary-features/uz@cyrillic.qm
%lang(vi) %{_datadir}/%{name}/translations/stellarium-planetary-features/vi.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/stellarium-planetary-features/zh_CN.qm
%lang(zh_HK) %{_datadir}/%{name}/translations/stellarium-planetary-features/zh_HK.qm
%lang(zh_SG) %{_datadir}/%{name}/translations/stellarium-planetary-features/zh_SG.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/stellarium-planetary-features/zh_TW.qm
%dir %{_datadir}/%{name}/translations/stellarium-remotecontrol
%lang(af) %{_datadir}/%{name}/translations/stellarium-remotecontrol/af.qm
%lang(ak) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ak.qm
%lang(am) %{_datadir}/%{name}/translations/stellarium-remotecontrol/am.qm
%lang(ar) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ar.qm
%lang(ast) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ast.qm
%lang(az) %{_datadir}/%{name}/translations/stellarium-remotecontrol/az.qm
%lang(be) %{_datadir}/%{name}/translations/stellarium-remotecontrol/be.qm
%lang(bg) %{_datadir}/%{name}/translations/stellarium-remotecontrol/bg.qm
%lang(bn) %{_datadir}/%{name}/translations/stellarium-remotecontrol/bn.qm
%lang(br) %{_datadir}/%{name}/translations/stellarium-remotecontrol/br.qm
%lang(bs) %{_datadir}/%{name}/translations/stellarium-remotecontrol/bs.qm
%lang(ca) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ca.qm
%lang(ca@valencia) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ca@valencia.qm
%lang(cnr) %{_datadir}/%{name}/translations/stellarium-remotecontrol/cnr.qm
%lang(cs) %{_datadir}/%{name}/translations/stellarium-remotecontrol/cs.qm
%lang(cv) %{_datadir}/%{name}/translations/stellarium-remotecontrol/cv.qm
%lang(da) %{_datadir}/%{name}/translations/stellarium-remotecontrol/da.qm
%lang(de) %{_datadir}/%{name}/translations/stellarium-remotecontrol/de.qm
%lang(el) %{_datadir}/%{name}/translations/stellarium-remotecontrol/el.qm
%lang(en) %{_datadir}/%{name}/translations/stellarium-remotecontrol/en.qm
%lang(en_AU) %{_datadir}/%{name}/translations/stellarium-remotecontrol/en_AU.qm
%lang(en_CA) %{_datadir}/%{name}/translations/stellarium-remotecontrol/en_CA.qm
%lang(en_GB) %{_datadir}/%{name}/translations/stellarium-remotecontrol/en_GB.qm
%lang(en_IN) %{_datadir}/%{name}/translations/stellarium-remotecontrol/en_IN.qm
%lang(en_US) %{_datadir}/%{name}/translations/stellarium-remotecontrol/en_US.qm
%lang(eo) %{_datadir}/%{name}/translations/stellarium-remotecontrol/eo.qm
%lang(es) %{_datadir}/%{name}/translations/stellarium-remotecontrol/es.qm
%lang(es_AR) %{_datadir}/%{name}/translations/stellarium-remotecontrol/es_AR.qm
%lang(es_CL) %{_datadir}/%{name}/translations/stellarium-remotecontrol/es_CL.qm
%lang(et) %{_datadir}/%{name}/translations/stellarium-remotecontrol/et.qm
%lang(eu) %{_datadir}/%{name}/translations/stellarium-remotecontrol/eu.qm
%lang(fa) %{_datadir}/%{name}/translations/stellarium-remotecontrol/fa.qm
%lang(fi) %{_datadir}/%{name}/translations/stellarium-remotecontrol/fi.qm
%lang(fr) %{_datadir}/%{name}/translations/stellarium-remotecontrol/fr.qm
%lang(fr_CA) %{_datadir}/%{name}/translations/stellarium-remotecontrol/fr_CA.qm
%lang(fy) %{_datadir}/%{name}/translations/stellarium-remotecontrol/fy.qm
%lang(ga) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ga.qm
%lang(gd) %{_datadir}/%{name}/translations/stellarium-remotecontrol/gd.qm
%lang(gl) %{_datadir}/%{name}/translations/stellarium-remotecontrol/gl.qm
%lang(gu) %{_datadir}/%{name}/translations/stellarium-remotecontrol/gu.qm
%lang(he) %{_datadir}/%{name}/translations/stellarium-remotecontrol/he.qm
%lang(hi) %{_datadir}/%{name}/translations/stellarium-remotecontrol/hi.qm
%lang(hr) %{_datadir}/%{name}/translations/stellarium-remotecontrol/hr.qm
%lang(hu) %{_datadir}/%{name}/translations/stellarium-remotecontrol/hu.qm
%lang(hy) %{_datadir}/%{name}/translations/stellarium-remotecontrol/hy.qm
%lang(id) %{_datadir}/%{name}/translations/stellarium-remotecontrol/id.qm
%lang(is) %{_datadir}/%{name}/translations/stellarium-remotecontrol/is.qm
%lang(it) %{_datadir}/%{name}/translations/stellarium-remotecontrol/it.qm
%lang(ja) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ja.qm
%lang(jv) %{_datadir}/%{name}/translations/stellarium-remotecontrol/jv.qm
%lang(ka) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ka.qm
%lang(kk) %{_datadir}/%{name}/translations/stellarium-remotecontrol/kk.qm
%lang(kn) %{_datadir}/%{name}/translations/stellarium-remotecontrol/kn.qm
%lang(ko) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ko.qm
%lang(krl) %{_datadir}/%{name}/translations/stellarium-remotecontrol/krl.qm
%lang(ku) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ku.qm
%lang(ky) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ky.qm
%lang(la) %{_datadir}/%{name}/translations/stellarium-remotecontrol/la.qm
%lang(lb) %{_datadir}/%{name}/translations/stellarium-remotecontrol/lb.qm
%lang(lt) %{_datadir}/%{name}/translations/stellarium-remotecontrol/lt.qm
%lang(lv) %{_datadir}/%{name}/translations/stellarium-remotecontrol/lv.qm
%lang(mk) %{_datadir}/%{name}/translations/stellarium-remotecontrol/mk.qm
%lang(ml) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ml.qm
%lang(mn) %{_datadir}/%{name}/translations/stellarium-remotecontrol/mn.qm
%lang(mr) %{_datadir}/%{name}/translations/stellarium-remotecontrol/mr.qm
%lang(ms) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ms.qm
%lang(my) %{_datadir}/%{name}/translations/stellarium-remotecontrol/my.qm
%lang(nb) %{_datadir}/%{name}/translations/stellarium-remotecontrol/nb.qm
%lang(nds) %{_datadir}/%{name}/translations/stellarium-remotecontrol/nds.qm
%lang(ne) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ne.qm
%lang(nl) %{_datadir}/%{name}/translations/stellarium-remotecontrol/nl.qm
%lang(nn) %{_datadir}/%{name}/translations/stellarium-remotecontrol/nn.qm
%lang(pa) %{_datadir}/%{name}/translations/stellarium-remotecontrol/pa.qm
%lang(pl) %{_datadir}/%{name}/translations/stellarium-remotecontrol/pl.qm
%lang(pt) %{_datadir}/%{name}/translations/stellarium-remotecontrol/pt.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/stellarium-remotecontrol/pt_BR.qm
%lang(ro) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ro.qm
%lang(ru) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ru.qm
%lang(sc) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sc.qm
%lang(si) %{_datadir}/%{name}/translations/stellarium-remotecontrol/si.qm
%lang(sk) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sk.qm
%lang(sl) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sl.qm
%lang(sq) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sq.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sr.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sr@latin.qm
%lang(sv) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sv.qm
%lang(sw) %{_datadir}/%{name}/translations/stellarium-remotecontrol/sw.qm
%lang(ta) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ta.qm
%lang(te) %{_datadir}/%{name}/translations/stellarium-remotecontrol/te.qm
%lang(tg) %{_datadir}/%{name}/translations/stellarium-remotecontrol/tg.qm
%lang(th) %{_datadir}/%{name}/translations/stellarium-remotecontrol/th.qm
%lang(tl) %{_datadir}/%{name}/translations/stellarium-remotecontrol/tl.qm
%lang(tr) %{_datadir}/%{name}/translations/stellarium-remotecontrol/tr.qm
%lang(tzm) %{_datadir}/%{name}/translations/stellarium-remotecontrol/tzm.qm
%lang(ug) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ug.qm
%lang(uk) %{_datadir}/%{name}/translations/stellarium-remotecontrol/uk.qm
%lang(ur) %{_datadir}/%{name}/translations/stellarium-remotecontrol/ur.qm
%lang(uz) %{_datadir}/%{name}/translations/stellarium-remotecontrol/uz.qm
%lang(uz) %{_datadir}/%{name}/translations/stellarium-remotecontrol/uz@cyrillic.qm
%lang(vi) %{_datadir}/%{name}/translations/stellarium-remotecontrol/vi.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/stellarium-remotecontrol/zh_CN.qm
%lang(zh_HK) %{_datadir}/%{name}/translations/stellarium-remotecontrol/zh_HK.qm
%lang(zh_SG) %{_datadir}/%{name}/translations/stellarium-remotecontrol/zh_SG.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/stellarium-remotecontrol/zh_TW.qm
%dir %{_datadir}/%{name}/translations/stellarium-scripts
%lang(af) %{_datadir}/%{name}/translations/stellarium-scripts/af.qm
%lang(ak) %{_datadir}/%{name}/translations/stellarium-scripts/ak.qm
%lang(am) %{_datadir}/%{name}/translations/stellarium-scripts/am.qm
%lang(ar) %{_datadir}/%{name}/translations/stellarium-scripts/ar.qm
%lang(ast) %{_datadir}/%{name}/translations/stellarium-scripts/ast.qm
%lang(az) %{_datadir}/%{name}/translations/stellarium-scripts/az.qm
%lang(be) %{_datadir}/%{name}/translations/stellarium-scripts/be.qm
%lang(bg) %{_datadir}/%{name}/translations/stellarium-scripts/bg.qm
%lang(bn) %{_datadir}/%{name}/translations/stellarium-scripts/bn.qm
%lang(br) %{_datadir}/%{name}/translations/stellarium-scripts/br.qm
%lang(bs) %{_datadir}/%{name}/translations/stellarium-scripts/bs.qm
%lang(ca) %{_datadir}/%{name}/translations/stellarium-scripts/ca.qm
%lang(ca@valencia) %{_datadir}/%{name}/translations/stellarium-scripts/ca@valencia.qm
%lang(cnr) %{_datadir}/%{name}/translations/stellarium-scripts/cnr.qm
%lang(cs) %{_datadir}/%{name}/translations/stellarium-scripts/cs.qm
%lang(cv) %{_datadir}/%{name}/translations/stellarium-scripts/cv.qm
%lang(da) %{_datadir}/%{name}/translations/stellarium-scripts/da.qm
%lang(de) %{_datadir}/%{name}/translations/stellarium-scripts/de.qm
%lang(el) %{_datadir}/%{name}/translations/stellarium-scripts/el.qm
%lang(en) %{_datadir}/%{name}/translations/stellarium-scripts/en.qm
%lang(en_AU) %{_datadir}/%{name}/translations/stellarium-scripts/en_AU.qm
%lang(en_CA) %{_datadir}/%{name}/translations/stellarium-scripts/en_CA.qm
%lang(en_GB) %{_datadir}/%{name}/translations/stellarium-scripts/en_GB.qm
%lang(en_IN) %{_datadir}/%{name}/translations/stellarium-scripts/en_IN.qm
%lang(en_US) %{_datadir}/%{name}/translations/stellarium-scripts/en_US.qm
%lang(eo) %{_datadir}/%{name}/translations/stellarium-scripts/eo.qm
%lang(es) %{_datadir}/%{name}/translations/stellarium-scripts/es.qm
%lang(es_AR) %{_datadir}/%{name}/translations/stellarium-scripts/es_AR.qm
%lang(es_CL) %{_datadir}/%{name}/translations/stellarium-scripts/es_CL.qm
%lang(et) %{_datadir}/%{name}/translations/stellarium-scripts/et.qm
%lang(eu) %{_datadir}/%{name}/translations/stellarium-scripts/eu.qm
%lang(fa) %{_datadir}/%{name}/translations/stellarium-scripts/fa.qm
%lang(fi) %{_datadir}/%{name}/translations/stellarium-scripts/fi.qm
%lang(fr) %{_datadir}/%{name}/translations/stellarium-scripts/fr.qm
%lang(fr_CA) %{_datadir}/%{name}/translations/stellarium-scripts/fr_CA.qm
%lang(fy) %{_datadir}/%{name}/translations/stellarium-scripts/fy.qm
%lang(ga) %{_datadir}/%{name}/translations/stellarium-scripts/ga.qm
%lang(gd) %{_datadir}/%{name}/translations/stellarium-scripts/gd.qm
%lang(gl) %{_datadir}/%{name}/translations/stellarium-scripts/gl.qm
%lang(gu) %{_datadir}/%{name}/translations/stellarium-scripts/gu.qm
%lang(he) %{_datadir}/%{name}/translations/stellarium-scripts/he.qm
%lang(hi) %{_datadir}/%{name}/translations/stellarium-scripts/hi.qm
%lang(hr) %{_datadir}/%{name}/translations/stellarium-scripts/hr.qm
%lang(hu) %{_datadir}/%{name}/translations/stellarium-scripts/hu.qm
%lang(hy) %{_datadir}/%{name}/translations/stellarium-scripts/hy.qm
%lang(id) %{_datadir}/%{name}/translations/stellarium-scripts/id.qm
%lang(is) %{_datadir}/%{name}/translations/stellarium-scripts/is.qm
%lang(it) %{_datadir}/%{name}/translations/stellarium-scripts/it.qm
%lang(ja) %{_datadir}/%{name}/translations/stellarium-scripts/ja.qm
%lang(jv) %{_datadir}/%{name}/translations/stellarium-scripts/jv.qm
%lang(ka) %{_datadir}/%{name}/translations/stellarium-scripts/ka.qm
%lang(kk) %{_datadir}/%{name}/translations/stellarium-scripts/kk.qm
%lang(kn) %{_datadir}/%{name}/translations/stellarium-scripts/kn.qm
%lang(ko) %{_datadir}/%{name}/translations/stellarium-scripts/ko.qm
%lang(krl) %{_datadir}/%{name}/translations/stellarium-scripts/krl.qm
%lang(ku) %{_datadir}/%{name}/translations/stellarium-scripts/ku.qm
%lang(ky) %{_datadir}/%{name}/translations/stellarium-scripts/ky.qm
%lang(la) %{_datadir}/%{name}/translations/stellarium-scripts/la.qm
%lang(lb) %{_datadir}/%{name}/translations/stellarium-scripts/lb.qm
%lang(lt) %{_datadir}/%{name}/translations/stellarium-scripts/lt.qm
%lang(lv) %{_datadir}/%{name}/translations/stellarium-scripts/lv.qm
%lang(mk) %{_datadir}/%{name}/translations/stellarium-scripts/mk.qm
%lang(ml) %{_datadir}/%{name}/translations/stellarium-scripts/ml.qm
%lang(mn) %{_datadir}/%{name}/translations/stellarium-scripts/mn.qm
%lang(mr) %{_datadir}/%{name}/translations/stellarium-scripts/mr.qm
%lang(ms) %{_datadir}/%{name}/translations/stellarium-scripts/ms.qm
%lang(my) %{_datadir}/%{name}/translations/stellarium-scripts/my.qm
%lang(nb) %{_datadir}/%{name}/translations/stellarium-scripts/nb.qm
%lang(nds) %{_datadir}/%{name}/translations/stellarium-scripts/nds.qm
%lang(ne) %{_datadir}/%{name}/translations/stellarium-scripts/ne.qm
%lang(nl) %{_datadir}/%{name}/translations/stellarium-scripts/nl.qm
%lang(nn) %{_datadir}/%{name}/translations/stellarium-scripts/nn.qm
%lang(pa) %{_datadir}/%{name}/translations/stellarium-scripts/pa.qm
%lang(pl) %{_datadir}/%{name}/translations/stellarium-scripts/pl.qm
%lang(pt) %{_datadir}/%{name}/translations/stellarium-scripts/pt.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/stellarium-scripts/pt_BR.qm
%lang(ro) %{_datadir}/%{name}/translations/stellarium-scripts/ro.qm
%lang(ru) %{_datadir}/%{name}/translations/stellarium-scripts/ru.qm
%lang(sc) %{_datadir}/%{name}/translations/stellarium-scripts/sc.qm
%lang(si) %{_datadir}/%{name}/translations/stellarium-scripts/si.qm
%lang(sk) %{_datadir}/%{name}/translations/stellarium-scripts/sk.qm
%lang(sl) %{_datadir}/%{name}/translations/stellarium-scripts/sl.qm
%lang(sq) %{_datadir}/%{name}/translations/stellarium-scripts/sq.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium-scripts/sr.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium-scripts/sr@latin.qm
%lang(sv) %{_datadir}/%{name}/translations/stellarium-scripts/sv.qm
%lang(sw) %{_datadir}/%{name}/translations/stellarium-scripts/sw.qm
%lang(ta) %{_datadir}/%{name}/translations/stellarium-scripts/ta.qm
%lang(te) %{_datadir}/%{name}/translations/stellarium-scripts/te.qm
%lang(tg) %{_datadir}/%{name}/translations/stellarium-scripts/tg.qm
%lang(th) %{_datadir}/%{name}/translations/stellarium-scripts/th.qm
%lang(tl) %{_datadir}/%{name}/translations/stellarium-scripts/tl.qm
%lang(tr) %{_datadir}/%{name}/translations/stellarium-scripts/tr.qm
%lang(tzm) %{_datadir}/%{name}/translations/stellarium-scripts/tzm.qm
%lang(ug) %{_datadir}/%{name}/translations/stellarium-scripts/ug.qm
%lang(uk) %{_datadir}/%{name}/translations/stellarium-scripts/uk.qm
%lang(ur) %{_datadir}/%{name}/translations/stellarium-scripts/ur.qm
%lang(uz) %{_datadir}/%{name}/translations/stellarium-scripts/uz.qm
%lang(uz) %{_datadir}/%{name}/translations/stellarium-scripts/uz@cyrillic.qm
%lang(vi) %{_datadir}/%{name}/translations/stellarium-scripts/vi.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/stellarium-scripts/zh_CN.qm
%lang(zh_HK) %{_datadir}/%{name}/translations/stellarium-scripts/zh_HK.qm
%lang(zh_SG) %{_datadir}/%{name}/translations/stellarium-scripts/zh_SG.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/stellarium-scripts/zh_TW.qm
%dir %{_datadir}/%{name}/translations/stellarium-skycultures
%lang(aa) %{_datadir}/%{name}/translations/stellarium-skycultures/aa.qm
%lang(ae) %{_datadir}/%{name}/translations/stellarium-skycultures/ae.qm
%lang(af) %{_datadir}/%{name}/translations/stellarium-skycultures/af.qm
%lang(ak) %{_datadir}/%{name}/translations/stellarium-skycultures/ak.qm
%lang(am) %{_datadir}/%{name}/translations/stellarium-skycultures/am.qm
%lang(ar) %{_datadir}/%{name}/translations/stellarium-skycultures/ar.qm
%lang(ast) %{_datadir}/%{name}/translations/stellarium-skycultures/ast.qm
%lang(av) %{_datadir}/%{name}/translations/stellarium-skycultures/av.qm
%lang(az) %{_datadir}/%{name}/translations/stellarium-skycultures/az.qm
%lang(be) %{_datadir}/%{name}/translations/stellarium-skycultures/be.qm
%lang(bg) %{_datadir}/%{name}/translations/stellarium-skycultures/bg.qm
%lang(bh) %{_datadir}/%{name}/translations/stellarium-skycultures/bh.qm
%lang(bi) %{_datadir}/%{name}/translations/stellarium-skycultures/bi.qm
%lang(bn) %{_datadir}/%{name}/translations/stellarium-skycultures/bn.qm
%lang(br) %{_datadir}/%{name}/translations/stellarium-skycultures/br.qm
%lang(bs) %{_datadir}/%{name}/translations/stellarium-skycultures/bs.qm
%lang(ca) %{_datadir}/%{name}/translations/stellarium-skycultures/ca.qm
%lang(ca@valencia) %{_datadir}/%{name}/translations/stellarium-skycultures/ca@valencia.qm
%lang(ce) %{_datadir}/%{name}/translations/stellarium-skycultures/ce.qm
%lang(cnr) %{_datadir}/%{name}/translations/stellarium-skycultures/cnr.qm
%lang(csb) %{_datadir}/%{name}/translations/stellarium-skycultures/csb.qm
%lang(cs) %{_datadir}/%{name}/translations/stellarium-skycultures/cs.qm
%lang(cv) %{_datadir}/%{name}/translations/stellarium-skycultures/cv.qm
%lang(da) %{_datadir}/%{name}/translations/stellarium-skycultures/da.qm
%lang(de) %{_datadir}/%{name}/translations/stellarium-skycultures/de.qm
%lang(el) %{_datadir}/%{name}/translations/stellarium-skycultures/el.qm
%lang(en) %{_datadir}/%{name}/translations/stellarium-skycultures/en.qm
%lang(en_AU) %{_datadir}/%{name}/translations/stellarium-skycultures/en_AU.qm
%lang(en_CA) %{_datadir}/%{name}/translations/stellarium-skycultures/en_CA.qm
%lang(en_GB) %{_datadir}/%{name}/translations/stellarium-skycultures/en_GB.qm
%lang(en_IN) %{_datadir}/%{name}/translations/stellarium-skycultures/en_IN.qm
%lang(en_US) %{_datadir}/%{name}/translations/stellarium-skycultures/en_US.qm
%lang(eo) %{_datadir}/%{name}/translations/stellarium-skycultures/eo.qm
%lang(es) %{_datadir}/%{name}/translations/stellarium-skycultures/es.qm
%lang(es_AR) %{_datadir}/%{name}/translations/stellarium-skycultures/es_AR.qm
%lang(es_CL) %{_datadir}/%{name}/translations/stellarium-skycultures/es_CL.qm
%lang(et) %{_datadir}/%{name}/translations/stellarium-skycultures/et.qm
%lang(eu) %{_datadir}/%{name}/translations/stellarium-skycultures/eu.qm
%lang(fa) %{_datadir}/%{name}/translations/stellarium-skycultures/fa.qm
%lang(fi) %{_datadir}/%{name}/translations/stellarium-skycultures/fi.qm
%lang(fj) %{_datadir}/%{name}/translations/stellarium-skycultures/fj.qm
%lang(fr) %{_datadir}/%{name}/translations/stellarium-skycultures/fr.qm
%lang(fr_CA) %{_datadir}/%{name}/translations/stellarium-skycultures/fr_CA.qm
%lang(fy) %{_datadir}/%{name}/translations/stellarium-skycultures/fy.qm
%lang(ga) %{_datadir}/%{name}/translations/stellarium-skycultures/ga.qm
%lang(gd) %{_datadir}/%{name}/translations/stellarium-skycultures/gd.qm
%lang(gl) %{_datadir}/%{name}/translations/stellarium-skycultures/gl.qm
%lang(gn) %{_datadir}/%{name}/translations/stellarium-skycultures/gn.qm
%lang(gu) %{_datadir}/%{name}/translations/stellarium-skycultures/gu.qm
%lang(gv) %{_datadir}/%{name}/translations/stellarium-skycultures/gv.qm
%lang(he) %{_datadir}/%{name}/translations/stellarium-skycultures/he.qm
%lang(hi) %{_datadir}/%{name}/translations/stellarium-skycultures/hi.qm
%lang(hr) %{_datadir}/%{name}/translations/stellarium-skycultures/hr.qm
%lang(hrx) %{_datadir}/%{name}/translations/stellarium-skycultures/hrx.qm
%lang(hu) %{_datadir}/%{name}/translations/stellarium-skycultures/hu.qm
%lang(hy) %{_datadir}/%{name}/translations/stellarium-skycultures/hy.qm
%lang(id) %{_datadir}/%{name}/translations/stellarium-skycultures/id.qm
%lang(is) %{_datadir}/%{name}/translations/stellarium-skycultures/is.qm
%lang(it) %{_datadir}/%{name}/translations/stellarium-skycultures/it.qm
%lang(ja) %{_datadir}/%{name}/translations/stellarium-skycultures/ja.qm
%lang(jv) %{_datadir}/%{name}/translations/stellarium-skycultures/jv.qm
%lang(ka) %{_datadir}/%{name}/translations/stellarium-skycultures/ka.qm
%lang(kg) %{_datadir}/%{name}/translations/stellarium-skycultures/kg.qm
%lang(kk) %{_datadir}/%{name}/translations/stellarium-skycultures/kk.qm
%lang(kn) %{_datadir}/%{name}/translations/stellarium-skycultures/kn.qm
%lang(ko) %{_datadir}/%{name}/translations/stellarium-skycultures/ko.qm
%lang(krl) %{_datadir}/%{name}/translations/stellarium-skycultures/krl.qm
%lang(ku) %{_datadir}/%{name}/translations/stellarium-skycultures/ku.qm
%lang(ky) %{_datadir}/%{name}/translations/stellarium-skycultures/ky.qm
%lang(la) %{_datadir}/%{name}/translations/stellarium-skycultures/la.qm
%lang(lb) %{_datadir}/%{name}/translations/stellarium-skycultures/lb.qm
%lang(lt) %{_datadir}/%{name}/translations/stellarium-skycultures/lt.qm
%lang(lv) %{_datadir}/%{name}/translations/stellarium-skycultures/lv.qm
%lang(mk) %{_datadir}/%{name}/translations/stellarium-skycultures/mk.qm
%lang(ml) %{_datadir}/%{name}/translations/stellarium-skycultures/ml.qm
%lang(mn) %{_datadir}/%{name}/translations/stellarium-skycultures/mn.qm
%lang(mo) %{_datadir}/%{name}/translations/stellarium-skycultures/mo.qm
%lang(moc) %{_datadir}/%{name}/translations/stellarium-skycultures/moc.qm
%lang(mr) %{_datadir}/%{name}/translations/stellarium-skycultures/mr.qm
%lang(ms) %{_datadir}/%{name}/translations/stellarium-skycultures/ms.qm
%lang(my) %{_datadir}/%{name}/translations/stellarium-skycultures/my.qm
%lang(na) %{_datadir}/%{name}/translations/stellarium-skycultures/na.qm
%lang(nb) %{_datadir}/%{name}/translations/stellarium-skycultures/nb.qm
%lang(nds) %{_datadir}/%{name}/translations/stellarium-skycultures/nds.qm
%lang(ne) %{_datadir}/%{name}/translations/stellarium-skycultures/ne.qm
%lang(nl) %{_datadir}/%{name}/translations/stellarium-skycultures/nl.qm
%lang(nn) %{_datadir}/%{name}/translations/stellarium-skycultures/nn.qm
%lang(oj) %{_datadir}/%{name}/translations/stellarium-skycultures/oj.qm
%lang(pa) %{_datadir}/%{name}/translations/stellarium-skycultures/pa.qm
%lang(pl) %{_datadir}/%{name}/translations/stellarium-skycultures/pl.qm
%lang(pt) %{_datadir}/%{name}/translations/stellarium-skycultures/pt.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/stellarium-skycultures/pt_BR.qm
%lang(ro) %{_datadir}/%{name}/translations/stellarium-skycultures/ro.qm
%lang(ru) %{_datadir}/%{name}/translations/stellarium-skycultures/ru.qm
%lang(sc) %{_datadir}/%{name}/translations/stellarium-skycultures/sc.qm
%lang(si) %{_datadir}/%{name}/translations/stellarium-skycultures/si.qm
%lang(sk) %{_datadir}/%{name}/translations/stellarium-skycultures/sk.qm
%lang(sl) %{_datadir}/%{name}/translations/stellarium-skycultures/sl.qm
%lang(sq) %{_datadir}/%{name}/translations/stellarium-skycultures/sq.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium-skycultures/sr.qm
%lang(sr) %{_datadir}/%{name}/translations/stellarium-skycultures/sr@latin.qm
%lang(sv) %{_datadir}/%{name}/translations/stellarium-skycultures/sv.qm
%lang(sw) %{_datadir}/%{name}/translations/stellarium-skycultures/sw.qm
%lang(ta) %{_datadir}/%{name}/translations/stellarium-skycultures/ta.qm
%lang(te) %{_datadir}/%{name}/translations/stellarium-skycultures/te.qm
%lang(tg) %{_datadir}/%{name}/translations/stellarium-skycultures/tg.qm
%lang(th) %{_datadir}/%{name}/translations/stellarium-skycultures/th.qm
%lang(tl) %{_datadir}/%{name}/translations/stellarium-skycultures/tl.qm
%lang(tr) %{_datadir}/%{name}/translations/stellarium-skycultures/tr.qm
%lang(tzm) %{_datadir}/%{name}/translations/stellarium-skycultures/tzm.qm
%lang(ug) %{_datadir}/%{name}/translations/stellarium-skycultures/ug.qm
%lang(uk) %{_datadir}/%{name}/translations/stellarium-skycultures/uk.qm
%lang(ur) %{_datadir}/%{name}/translations/stellarium-skycultures/ur.qm
%lang(uz) %{_datadir}/%{name}/translations/stellarium-skycultures/uz.qm
%lang(uz) %{_datadir}/%{name}/translations/stellarium-skycultures/uz@cyrillic.qm
%lang(vi) %{_datadir}/%{name}/translations/stellarium-skycultures/vi.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/stellarium-skycultures/zh_CN.qm
%lang(zh_HK) %{_datadir}/%{name}/translations/stellarium-skycultures/zh_HK.qm
%lang(zh_SG) %{_datadir}/%{name}/translations/stellarium-skycultures/zh_SG.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/stellarium-skycultures/zh_TW.qm
