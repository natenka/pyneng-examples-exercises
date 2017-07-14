create table if not exists dhcp (
    mac          text primary key,
    ip           text,
    vlan         text,
    interface    text
);
