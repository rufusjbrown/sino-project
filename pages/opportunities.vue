<template>
    <section>
        <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
                v-model="name"
                label="Name"
                solo>
            </v-text-field>
            <v-text-field
                v-model="email"
                :rules="emailRules"
                label="E-mail"
                required
                solo>
            </v-text-field>
            <v-select
                :items="countryList"
                :rules="[v => !!v || 'Item is required']"
                label="Nationality"
                v-model="nationality"
                item-text="name"
                solo>
            </v-select>
            <v-select
                :items="experienceList"
                :rules="[v => !!v || 'Item is required']"
                v-model="experience"
                label="Experience"
                item-text="desc"
                solo>
            </v-select>
            <v-menu
                ref="menu"
                :close-on-content-click="false"
                v-model="menu"
                :nudge-right="40"
                :rules="[v => !!v || 'Item is required']"
                :return-value.sync="date"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                max-width="290px"
                min-width="290px">
                <v-text-field
                    slot="activator"
                    v-model="date"
                    label="Earliest Start Date"
                    prepend-icon="event"
                    readonly>
                </v-text-field>
                <v-date-picker
                    v-model="date"
                    type="month"
                    no-title
                    scrollable
                    >
                    <v-spacer></v-spacer>
                    <v-btn flat color="primary" @click="menu = false">Cancel</v-btn>
                    <v-btn flat color="primary" @click="$refs.menu.save(date)">OK</v-btn>
                </v-date-picker>
            </v-menu>
            <v-select
                :items="preferredLocation"
                v-model="location"
                :rules="[v => !!v || 'Item is required']"
                label="Preferred Location"
                item-text="desc"
                solo>
            </v-select>
            <v-select
                :items="qualifications"
                :rules="[v => !!v || 'Item is required']"
                :menu-props="{ maxHeight: '400' }"
                v-model="qualification"
                label="Qualifications"
                item-text="desc"
                multiple                
                persistent-hint
                solo>
            </v-select>
            <v-select
                :items="positionSeeking"
                :rules="[v => !!v || 'Item is required']"
                :menu-props="{ maxHeight: '400' }"
                v-model="position"
                label="What type of position are you seeking?"
                item-text="desc"
                multiple
                persistent-hint
                solo>
            </v-select>
            <v-btn :disabled="!valid" @click="submit">submit</v-btn>
            <v-btn @click="clear">clear</v-btn>
        </v-form>
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
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      valid: true,
      name: '',
      email: '',
      nationality: '',
      experience: '',
      location: '',
      qualification: '',
      position: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 30) || 'Name must be less than 30 characters'
      ],
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid'
      ],
      users: ''
    }),
    methods: {
      submit () {
        if (this.$refs.form.validate()) {
          // Native form submission is not yet supported
          axios.post('https://rufusbrown.pythonanywhere.com/api/submit', {
            name: this.name,
            email: this.email,
            nationality: this.nationality,
            experience: this.experience,
            startDate: this.date,
            preferredLocation: this.location,
            qualifications: this.qualification,
            positionSeeked: this.position
          })
          console.log({
            name: this.name,
            email: this.email,
            nationality: this.nationality,
            experience: this.experience,
            startDate: this.date,
            preferredLocation: this.location,
            qualifications: this.qualification,
            positionSeeked: this.position
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
