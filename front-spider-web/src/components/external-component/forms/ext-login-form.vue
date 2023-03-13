<template>
    <!--
    This example requires updating your template:

    ```
    <html class="h-full bg-gray-50">
    <body class="h-full">
    ```
  -->
    <div class="tw-flex tw-min-h-full tw-items-center tw-justify-center tw-py-12 tw-px-4 sm:tw-px-6 lg:tw-px-8">
        <div class="tw-w-full tw-max-w-md tw-space-y-8">
            <div>
                <img
                    alt="Your Company"
                    class="tw-mx-auto tw-h-12 tw-w-auto"
                    src="https://tailwindui.com/img/logos/mark.svg?color=indigo&amp;shade=600"
                />
                <h2 class="tw-mt-6 tw-text-center tw-text-3xl tw-font-bold tw-tracking-tight tw-text-gray-900">Login</h2>
            </div>
            <form action="#" class="tw-mt-8 tw-space-y-6" method="POST">
                <input name="remember" type="hidden" value="true" />
                <div class="tw--space-y-px tw-rounded-md tw-shadow-sm">
                    <div>
                        <label class="tw-sr-only" for="ext-login-form-email-address">Email address</label>
                        <extInput
                            id="email-address"
                            autocomplete="email"
                            name="email"
                            placeholder="Email address"
                            required=""
                            type="email"
                            class="tw-mb-4 tw-w-full"
                        />
                    </div>
                    <div>
                        <label class="tw-sr-only" for="ext-login-form-password">Password</label>
                        <extInput
                            id="ext-login-form-password"
                            autocomplete="current-password"
                            name="password"
                            placeholder="Password"
                            required=""
                            type="password"
                            class="tw-w-full"
                        />
                    </div>
                </div>
                <div class="tw-flex tw-items-center tw-justify-between">
                    <div class="tw-flex tw-items-center">
                        <input
                            class="tw-h-4 tw-w-4 tw-rounded tw-border-gray-300 tw-text-indigo-600 focus:tw-ring-indigo-600"
                            id="remember-me"
                            name="remember-me"
                            type="checkbox"
                        />
                        <label class="tw-ml-2 tw-block tw-text-sm tw-text-gray-900" for="remember-me">Remember me</label>
                    </div>
                    <div class="tw-text-sm">
                        <a class="tw-font-medium tw-text-indigo-600 hover:tw-text-indigo-500" href="#"
                            >Forgot your password?</a
                        >
                    </div>
                </div>
                <div>
                    <extButton class="tw-group tw-relative tw-flex tw-w-full tw-justify-center" type="submit">
                        Sign in
                    </extButton>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import extInput from './ext-input.vue'
import extButton from '../atomic/ext-button.vue'
</script>
