{ pkgs }: {
  deps = [
    pkgs.postgresql_14
    pkgs.sudo
    pkgs.python38Full
  ];
  env = {
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}