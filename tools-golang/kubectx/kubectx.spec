%global debug_package %{nil}

Name:       kubectx
# renovate: datasource=github-releases depName=ahmetb/kubectx extractVersion=true
Version:    0.11.0
Release:    1%{?dist}
Summary:    Faster way to switch between clusters and namespaces in kubectl
License:    Apache-2.0
URL:        https://github.com/ahmetb/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang

%description

%prep
%autosetup -n %{name}-%{version}

%build
export GOTOOLCHAIN=auto
go build \
    -ldflags "-X main.version=v%{version} -s -w" \
    -o _build/%{name} \
	./cmd/%{name}
go build \
    -ldflags "-X main.version=v%{version} -s -w" \
    -o _build/kubens \
	./cmd/kubens
go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}
install -Dpm 0755 _build/kubens -t %{buildroot}%{_bindir}
install -Dpm 0644 %{name}.1 -t %{buildroot}/%{_mandir}/man1/
install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
install -Dpm 0644 completion/%{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm 0644 completion/%{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm 0644 completion/_%{name}.zsh %{buildroot}%{zsh_completions_dir}/_%{name}
install -Dpm 0644 completion/kubens.bash %{buildroot}%{bash_completions_dir}/kubens
install -Dpm 0644 completion/kubens.fish %{buildroot}%{fish_completions_dir}/kubens.fish
install -Dpm 0644 completion/_kubens.zsh %{buildroot}%{zsh_completions_dir}/_kubens

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/kubens
%{_mandir}/man1/*.1*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}
%{bash_completions_dir}/kubens
%{fish_completions_dir}/kubens.fish
%{zsh_completions_dir}/_kubens

%changelog
%autochangelog
