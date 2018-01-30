# flake8: noqa

from cytoolz import (
    curry,
)

from eth_utils import (
    add_0x_prefix,
    apply_formatter_at_index,
    apply_formatter_if,
    apply_formatter_to_array,
    apply_formatters_to_dict,
    apply_key_map,
    apply_one_of_formatters,
    apply_to_return_value,
    big_endian_to_int,
    coerce_args_to_bytes,
    coerce_args_to_text,
    coerce_return_to_bytes,
    coerce_return_to_text,
    combine_argument_formatters,
    combomethod,
    decode_hex,
    denoms,
    encode_hex,
    event_abi_to_log_topic,
    event_signature_to_log_topic,
    flatten_return,
    force_bytes,
    force_obj_to_bytes,
    force_obj_to_text,
    force_text,
    from_wei,
    function_abi_to_4byte_selector,
    function_signature_to_4byte_selector,
    hexstr_if_str,
    int_to_big_endian,
    is_0x_prefixed,
    is_32byte_address,
    is_address,
    is_binary_address,
    is_boolean,
    is_bytes,
    is_canonical_address,
    is_checksum_address,
    is_checksum_formatted_address,
    is_dict,
    is_hex,
    is_hex_address,
    is_integer,
    is_list_like,
    is_normalized_address,
    is_null,
    is_number,
    is_same_address,
    is_string,
    is_text,
    keccak,
    pad_left,
    pad_right,
    remove_0x_prefix,
    reversed_return,
    sort_return,
    text_if_str,
    to_bytes,
    to_canonical_address,
    to_checksum_address,
    to_dict,
    to_hex,
    to_int,
    to_list,
    to_normalized_address,
    to_ordered_dict,
    to_set,
    to_text,
    to_tuple,
    to_wei,
)

apply_formatter_at_index = curry(apply_formatter_at_index)
apply_formatter_if = curry(apply_formatter_if)
apply_formatter_to_array = curry(apply_formatter_to_array)
apply_formatters_to_dict = curry(apply_formatters_to_dict)
apply_key_map = curry(apply_key_map)
apply_one_of_formatters = curry(apply_one_of_formatters)
flatten_return = curry(flatten_return)
force_bytes = curry(force_bytes)
force_text = curry(force_text)
from_wei = curry(from_wei)
hexstr_if_str = curry(hexstr_if_str)
is_same_address = curry(is_same_address)
pad_left = curry(pad_left)
pad_right = curry(pad_right)
reversed_return = curry(reversed_return)
sort_return = curry(sort_return)
text_if_str = curry(text_if_str)
to_wei = curry(to_wei)

del curry