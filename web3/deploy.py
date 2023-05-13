import solcx

solcx.install_solc("1.1.1")

with open("./SimpleStorage.sol", "r") as file:
    simple_store_file = file.read()


# Compile our Solidity

compiled_sol = solcx.compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_store_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="1.1.1",
)

print(compiled_sol)
