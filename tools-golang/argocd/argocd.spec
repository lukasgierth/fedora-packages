%global debug_package %{nil}

Name:       argocd
# renovate: datasource=github-releases depName=argoproj/argo-cd extractVersion=true
Version:    3.3.9
Release:    1%{?dist}
Summary:    Declarative Continuous Deployment for Kubernetes
License:    Apache-2.0
URL:        https://github.com/argoproj/argo-cd
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang

%description

%prep
%autosetup -n argo-cd-%{version}

%build
export GOTOOLCHAIN=auto
export BUILD_DATE=$(date --iso-8601)
go build \
    -ldflags "-X github.com/argoproj/argo-cd/v3/common.version=%{version} -X github.com/argoproj/argo-cd/v3/common.buildDate=${BUILD_DATE} -s -w" \
    -o _build/%{name} \
	./cmd
go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}/
install -Dpm 0644 %{name}.1 -t %{buildroot}/%{_mandir}/man1/
install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
_build/%{name} completion bash > %{buildroot}%{bash_completions_dir}/%{name}
_build/%{name} completion fish > %{buildroot}%{fish_completions_dir}/%{name}.fish
_build/%{name} completion zsh > %{buildroot}%{zsh_completions_dir}/_%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
