const parametersToObject = (arguments_obj) => {
    let parameters_object = {}
    Object.keys(arguments_obj).forEach((key) => {
        if (arguments_obj[key]) parameters_object[key] = arguments_obj[key]
    })
}

export { parametersToObject }
