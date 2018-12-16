<template>
    <section>
        <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
            v-model="name"
            :rules="nameRules"
            :counter="30"
            label="Name"
            required
            solo
            ></v-text-field>
            <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            solo
            ></v-text-field>
            <v-select
            v-model="select"
            :items="items"
            :rules="[v => !!v || 'Item is required']"
            label="Item"
            required
            solo
            ></v-select>
            <v-select
                :items="countryList"
                label="Nationality"
                item-text="name"
                solo>
            </v-select>
            <v-select
                :items="experienceList"
                label="Experience"
                item-text="desc"
                solo>
            </v-select>
            <v-menu
                ref="menu"
                :close-on-content-click="false"
                v-model="menu"
                :nudge-right="40"
                :return-value.sync="date"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                min-width="290px"
            >
                <v-text-field
                slot="activator"
                v-model="date"
                label="Picker in menu"
                prepend-icon="event"
                readonly
                ></v-text-field>
                <v-date-picker v-model="date" no-title scrollable>
                <v-spacer></v-spacer>
                <v-btn flat color="primary" @click="menu = false">Cancel</v-btn>
                <v-btn flat color="primary" @click="$refs.menu.save(date)">OK</v-btn>
                </v-date-picker>
            </v-menu>
            <v-select
                :items="preferredLocation"
                label="Preferred Location"
                item-text="desc"
                solo>
            </v-select>
            <v-select
                :items="qualifications"
                :menu-props="{ maxHeight: '400' }"
                label="Qualifications"
                item-text="desc"
                multiple                
                persistent-hint
                solo>
            </v-select>
            <v-select
                :items="positionSeeking"
                :menu-props="{ maxHeight: '400' }"
                label="What type of position are you seeking?"
                item-text="desc"
                multiple
                persistent-hint
                solo>
            </v-select>
            <v-checkbox
            v-model="checkbox"
            :rules="[v => !!v || 'You must agree to continue!']"
            label="Do you agree?"
            required
            ></v-checkbox>

            <v-btn
            :disabled="!valid"
            @click="submit"
            >
            submit
            </v-btn>
            <v-btn @click="clear">clear</v-btn>
        </v-form>
        <ul>
            <li v-for="user in users" :key="user.name">
                {{ user.name }} -- {{ user.email }}
            </li>
        </ul>
    </section>
</template>

<script>
  import axios from 'axios'
  import { countryList, experienceList, preferredLocation, qualifications, positionSeeking } from '../plugins/form-dropdown-lists'

  export default {
    data: () => ({
      countryList: countryList,
      experienceList: experienceList,
      preferredLocation: preferredLocation,
      qualifications: qualifications,
      positionSeeking: positionSeeking,
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 30) || 'Name must be less than 30 characters'
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
      select: null,
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4'
      ],
      checkbox: false,
      users: ''
    }),
    methods: {
      submit () {
        if (this.$refs.form.validate()) {
          // Native form submission is not yet supported
          axios.post('https://rufusbrown.pythonanywhere.com/api/submit', {
            name: this.name,
            email: this.email
          })
          console.log({
            name: this.name,
            email: this.email,
            select: this.select,
            checkbox: this.checkbox
          })
        }
        this.getUsers()
      },
      clear () {
        this.$refs.form.reset()
      },
      getUsers () {
        axios.get('https://rufusbrown.pythonanywhere.com/api/getUsers')
          .then(res => {
            this.users = res.data
          })
      }
    },
    created () {
      this.getUsers()
    }
  }
</script>
